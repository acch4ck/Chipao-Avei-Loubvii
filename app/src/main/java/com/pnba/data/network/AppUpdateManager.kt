package com.pnba.data.network

import android.content.Context
import com.pnba.util.AppNotificationManager
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONObject
import java.io.BufferedReader
import java.net.HttpURLConnection
import java.net.URL

data class AppUpdateInfo(
    val isUpdateAvailable: Boolean,
    val currentVersion: String,
    val latestVersion: String,
    val latestVersionCode: Int,
    val releaseNotes: String,
    val downloadUrl: String
)

object AppUpdateManager {
    const val CURRENT_VERSION_CODE = 2
    const val CURRENT_VERSION_NAME = "1.1"

    suspend fun checkForUpdates(context: Context): Result<AppUpdateInfo> = withContext(Dispatchers.IO) {
        val checkUrl = FeedbackConfig.UPDATE_CHECK_URL.ifBlank {
            if (FeedbackConfig.WEBHOOK_URL.isNotBlank()) {
                "${FeedbackConfig.WEBHOOK_URL}?action=check_update"
            } else ""
        }

        if (checkUrl.isBlank()) {
            return@withContext Result.success(
                AppUpdateInfo(
                    isUpdateAvailable = false,
                    currentVersion = CURRENT_VERSION_NAME,
                    latestVersion = CURRENT_VERSION_NAME,
                    latestVersionCode = CURRENT_VERSION_CODE,
                    releaseNotes = "You are on the latest version.",
                    downloadUrl = ""
                )
            )
        }

        try {
            val url = URL(checkUrl)
            val connection = (url.openConnection() as HttpURLConnection).apply {
                requestMethod = "GET"
                connectTimeout = 10000
                readTimeout = 10000
                instanceFollowRedirects = true
                setRequestProperty("User-Agent", "ChipaoAveiLoubvu-Android")
                setRequestProperty("Accept", "application/json")
            }

            val responseCode = connection.responseCode
            if (responseCode in 200..299) {
                val jsonString = connection.inputStream.bufferedReader().use(BufferedReader::readText)
                connection.disconnect()
                val json = JSONObject(jsonString)
                val latestCode = json.optInt("latestVersionCode", CURRENT_VERSION_CODE)
                val latestName = json.optString("latestVersionName", CURRENT_VERSION_NAME)
                val notes = json.optString("releaseNotes", "")
                val downloadUrl = json.optString("downloadUrl", "")

                val updateAvailable = latestCode > CURRENT_VERSION_CODE
                if (updateAvailable) {
                    AppNotificationManager.showUpdateNotification(
                        context = context,
                        latestVersionName = latestName,
                        releaseNotes = notes,
                        downloadUrl = downloadUrl
                    )
                }

                Result.success(
                    AppUpdateInfo(
                        isUpdateAvailable = updateAvailable,
                        currentVersion = CURRENT_VERSION_NAME,
                        latestVersion = latestName,
                        latestVersionCode = latestCode,
                        releaseNotes = notes,
                        downloadUrl = downloadUrl
                    )
                )
            } else {
                connection.disconnect()
                Result.failure(Exception("HTTP $responseCode from update server"))
            }
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
