package com.pnba.util

import android.Manifest
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import androidx.core.content.ContextCompat
import com.pnba.R

object AppNotificationManager {
    const val CHANNEL_ID_UPDATES = "pnba_app_updates"
    private const val NOTIFICATION_ID_UPDATE = 1001

    fun createNotificationChannels(context: Context) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val name = "App Updates & Releases"
            val descriptionText = "Notifications for new hymnbook releases and updates"
            val importance = NotificationManager.IMPORTANCE_DEFAULT
            val channel = NotificationChannel(CHANNEL_ID_UPDATES, name, importance).apply {
                description = descriptionText
            }
            val notificationManager: NotificationManager =
                context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
            notificationManager.createNotificationChannel(channel)
        }
    }

    fun showUpdateNotification(
        context: Context,
        latestVersionName: String,
        releaseNotes: String,
        downloadUrl: String
    ) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            if (ContextCompat.checkSelfPermission(
                    context,
                    Manifest.permission.POST_NOTIFICATIONS
                ) != PackageManager.PERMISSION_GRANTED
            ) {
                return
            }
        }

        createNotificationChannels(context)

        val intent = if (downloadUrl.isNotBlank()) {
            Intent(Intent.ACTION_VIEW, Uri.parse(downloadUrl))
        } else {
            context.packageManager.getLaunchIntentForPackage(context.packageName) ?: Intent()
        }

        val pendingIntent = PendingIntent.getActivity(
            context,
            0,
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        val builder = NotificationCompat.Builder(context, CHANNEL_ID_UPDATES)
            .setSmallIcon(R.drawable.pnba_logo)
            .setContentTitle("Update Available: v$latestVersionName")
            .setContentText(releaseNotes.ifBlank { "A new version of Chipao Avei Loubvü is ready to install." })
            .setStyle(
                NotificationCompat.BigTextStyle()
                    .bigText(releaseNotes.ifBlank { "A new version of Chipao Avei Loubvü is available with new hymns and refinements. Tap to download." })
            )
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .setContentIntent(pendingIntent)
            .setAutoCancel(true)

        try {
            NotificationManagerCompat.from(context).notify(NOTIFICATION_ID_UPDATE, builder.build())
        } catch (_: SecurityException) {
            // Notification permission not granted
        }
    }
}
