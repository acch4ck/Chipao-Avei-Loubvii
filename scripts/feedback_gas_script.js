/**
 * Google Apps Script - Chipao Avei Loubvü Feedback Handler
 *
 * SETUP INSTRUCTIONS:
 * 1. Go to https://script.google.com and open your project
 * 2. Replace doPost(e) with this entire script
 * 3. Click Deploy → Manage deployments → Edit (pencil icon)
 * 4. Set Version = "New version"
 * 5. Set "Who has access" = "Anyone"
 * 6. Click Deploy
 * 7. If the URL changes, update FeedbackConfig.kt WEBHOOK_URL and rebuild the app
 *
 * EMAIL BEHAVIOUR:
 * - TO:      onisimuslanamai@gmail.com  (developer receives all feedback)
 * - REPLY-TO: user's email (if they provided one) — so replies go back to the user
 * - FROM:    always your Google account (GAS limitation — cannot spoof From)
 */

function doPost(e) {
  try {
    // Parse JSON body sent by the Android app
    const body = JSON.parse(e.postData.contents);

    const hymn        = body.hymn    || "(not specified)";
    const detail      = body.detail  || "(no detail)";
    const senderName  = body.name    || "Anonymous";
    const senderEmail = body.email   || "";
    const platform    = body.app     || "Chipao Avei Loubvü";

    const recipient = "onisimuslanamai@gmail.com"; // Developer's email (TO)

    const subject = `Chipao Avei Loubvü Feedback: Hymn #${hymn}`;

    const bodyText =
      `Hymn: ${hymn}\n` +
      `Details / Typo Correction:\n${detail}\n\n` +
      `----------------------\n` +
      `Submitted By: ${senderName}\n` +
      `Sender Email: ${senderEmail || "(not provided)"}\n` +
      `Platform: ${platform}`;

    const options = {
      name: senderName || "App User"
    };

    // If user provided their email, set replyTo so developer can reply directly to them
    if (senderEmail && senderEmail.includes("@")) {
      options.replyTo = senderEmail;
    }

    MailApp.sendEmail(recipient, subject, bodyText, options);

    return ContentService
      .createTextOutput(JSON.stringify({ status: "ok", message: "Feedback received!" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/** Optional: test function to verify email works in GAS editor */
function testDoPost() {
  const mockEvent = {
    postData: {
      contents: JSON.stringify({
        hymn: "2",
        detail: "Test correction",
        name: "Test User",
        email: "testuser@example.com",
        app: "Chipao Avei Loubvü Android"
      })
    }
  };
  const result = doPost(mockEvent);
  Logger.log(result.getContent());
}
