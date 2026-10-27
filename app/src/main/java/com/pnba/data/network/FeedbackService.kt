package com.pnba.data.network

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONObject
import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.net.HttpURLConnection
import java.net.URL

object FeedbackService {

    suspend fun sendFeedback(
        hymnNumber: String,
        typoDetail: String,
        senderName: String,
        senderEmail: String
    ): Result<String> = withContext(Dispatchers.IO) {
        val webhookUrl = FeedbackConfig.WEBHOOK_URL.trim()
        if (webhookUrl.isBlank()) {
            return@withContext Result.failure(
                IllegalStateException("Webhook URL has not been configured in FeedbackConfig.kt yet.")
            )
        }

        try {
            val jsonPayload = JSONObject().apply {
                put("hymn", hymnNumber.trim())
                put("detail", typoDetail.trim())
                put("name", senderName.trim())
                put("email", senderEmail.trim())
                put("timestamp", System.currentTimeMillis())
                put("app", "Chipao Avei Loubvü Android")
            }.toString()

            var currentUrl = webhookUrl
            var connection: HttpURLConnection? = null
            var redirectCount = 0
            val maxRedirects = 5

            while (redirectCount < maxRedirects) {
                val url = URL(currentUrl)
                connection = (url.openConnection() as HttpURLConnection).apply {
                    requestMethod = if (redirectCount == 0) "POST" else "GET"
                    connectTimeout = 15000
                    readTimeout = 15000
                    instanceFollowRedirects = false
                    setRequestProperty("User-Agent", "ChipaoAveiLoubvu-Android")
                    setRequestProperty("Accept", "application/json, text/plain, */*")
                    if (redirectCount == 0) {
                        doOutput = true
                        setRequestProperty("Content-Type", "application/json; charset=UTF-8")
                    }
                }

                if (redirectCount == 0) {
                    OutputStreamWriter(connection.outputStream, "UTF-8").use { writer ->
                        writer.write(jsonPayload)
                        writer.flush()
                    }
                }

                val responseCode = connection.responseCode

                // Google Apps Script redirects with 302 to return the output
                if (responseCode == HttpURLConnection.HTTP_MOVED_TEMP ||
                    responseCode == HttpURLConnection.HTTP_MOVED_PERM ||
                    responseCode == HttpURLConnection.HTTP_SEE_OTHER ||
                    responseCode == 307
                ) {
                    val newLocation = connection.getHeaderField("Location")
                    connection.disconnect()
                    if (!newLocation.isNullOrBlank()) {
                        currentUrl = newLocation
                        redirectCount++
                        continue
                    } else {
                        // Redirect with no Location header, but POST was accepted
                        return@withContext Result.success("Feedback sent successfully!")
                    }
                }

                if (responseCode in 200..299) {
                    val responseText = connection.inputStream.bufferedReader().use(BufferedReader::readText)
                    connection.disconnect()
                    return@withContext Result.success(responseText.ifBlank { "Feedback sent successfully!" })
                } else {
                    val errorText = connection.errorStream?.bufferedReader()?.use(BufferedReader::readText) ?: ""
                    connection.disconnect()
                    val userMsg = if (responseCode == 403) {
                        "Google permission error (403): Web app access is restricted. In script.google.com -> Deploy -> Manage deployments -> set 'Who has access' to 'Anyone'."
                    } else {
                        "Server error ($responseCode)"
                    }
                    return@withContext Result.failure(Exception(userMsg))
                }
            }

            // If we completed redirects
            Result.success("Feedback sent successfully!")
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
