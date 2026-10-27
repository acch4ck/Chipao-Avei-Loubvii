package com.pnba.sound

import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioTrack
import com.pnba.data.model.MelodyNote
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import kotlin.math.sin

object PitchPipePlayer {
    private var currentJob: Job? = null
    private val scope = CoroutineScope(Dispatchers.Default)

    /**
     * Standard pitch frequencies (in Hz) for the octave
     */
    val STANDARD_PITCHES = mapOf(
        "C4" to 261.63f,
        "D4" to 293.66f,
        "E4" to 329.63f,
        "F4" to 349.23f,
        "G4" to 392.00f,
        "A4" to 440.00f,
        "B4" to 493.88f,
        "C5" to 523.25f
    )

    fun playSinglePitch(frequencyHz: Float, durationMs: Long = 1800L, onFinished: (() -> Unit)? = null) {
        stop()
        currentJob = scope.launch {
            try {
                playTone(frequencyHz, durationMs)
            } catch (e: Exception) {
                if (e is CancellationException) throw e
            } finally {
                withContext(Dispatchers.Main) {
                    onFinished?.invoke()
                }
            }
        }
    }

    fun playMelody(notes: List<MelodyNote>, onFinished: (() -> Unit)? = null) {
        if (notes.isEmpty()) {
            onFinished?.invoke()
            return
        }
        stop()
        currentJob = scope.launch {
            try {
                for (note in notes) {
                    if (!isActive) break
                    playTone(note.pitchHz, note.durationMs)
                    delay(50L) // Subtle breath between notes
                }
            } catch (e: Exception) {
                if (e is CancellationException) throw e
            } finally {
                withContext(Dispatchers.Main) {
                    onFinished?.invoke()
                }
            }
        }
    }

    fun stop() {
        currentJob?.cancel()
        currentJob = null
    }

    private suspend fun playTone(frequencyHz: Float, durationMs: Long) = withContext(Dispatchers.Default) {
        val sampleRate = 44100
        val numSamples = ((durationMs / 1000.0) * sampleRate).toInt()
        val generatedSnd = ShortArray(numSamples)

        val fadeDuration = (0.04 * sampleRate).toInt() // 40ms attack and release envelope

        for (i in 0 until numSamples) {
            val t = i.toDouble() / sampleRate
            // Main fundamental wave + gentle first harmonic for rich warm choir pitch pipe tone
            val fundamental = sin(2.0 * Math.PI * frequencyHz * t)
            val harmonic1 = 0.25 * sin(2.0 * Math.PI * frequencyHz * 2.0 * t)
            val harmonic2 = 0.1 * sin(2.0 * Math.PI * frequencyHz * 3.0 * t)
            var sample = (fundamental + harmonic1 + harmonic2) / 1.35

            // Envelope smoothing to prevent clicks
            if (i < fadeDuration) {
                sample *= (i.toDouble() / fadeDuration)
            } else if (i > numSamples - fadeDuration) {
                sample *= ((numSamples - i).toDouble() / fadeDuration)
            }

            generatedSnd[i] = (sample * 0.75 * Short.MAX_VALUE).toInt().toShort()
        }

        var track: AudioTrack? = null
        try {
            val minBufferSize = AudioTrack.getMinBufferSize(
                sampleRate,
                AudioFormat.CHANNEL_OUT_MONO,
                AudioFormat.ENCODING_PCM_16BIT
            )
            val bufferSize = maxOf(minBufferSize, numSamples * 2)

            track = AudioTrack.Builder()
                .setAudioAttributes(
                    AudioAttributes.Builder()
                        .setUsage(AudioAttributes.USAGE_MEDIA)
                        .setContentType(AudioAttributes.CONTENT_TYPE_MUSIC)
                        .build()
                )
                .setAudioFormat(
                    AudioFormat.Builder()
                        .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
                        .setSampleRate(sampleRate)
                        .setChannelMask(AudioFormat.CHANNEL_OUT_MONO)
                        .build()
                )
                .setBufferSizeInBytes(bufferSize)
                .setTransferMode(AudioTrack.MODE_STATIC)
                .build()

            track.write(generatedSnd, 0, numSamples)
            track.play()
            delay(durationMs)
        } catch (_: Exception) {
            // Ignore track errors gracefully
        } finally {
            try {
                track?.stop()
                track?.release()
            } catch (_: Exception) {
            }
        }
    }
}
