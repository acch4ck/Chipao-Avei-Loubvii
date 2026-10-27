package com.pnba.ui.theme

import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.tween
import androidx.compose.material3.ColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import com.pnba.data.model.ReadingTheme

// 1. Parchment (Default Classic Hymnal)
val ParchmentColorScheme = lightColorScheme(
    primary = SanctuaryNavy,
    onPrimary = Color.White,
    primaryContainer = ParchmentSurfaceAlt,
    onPrimaryContainer = SanctuaryNavy,
    secondary = GoldBrass,
    onSecondary = Color.White,
    secondaryContainer = ParchmentSurfaceAlt,
    onSecondaryContainer = SanctuaryNavy,
    tertiary = ChancelBurgundy,
    background = ParchmentBg,
    onBackground = ParchmentInk,
    surface = ParchmentSurface,
    onSurface = ParchmentInk,
    surfaceVariant = ParchmentSurfaceAlt,
    onSurfaceVariant = ParchmentInkMuted
)

// 2. Midnight Navy
val NavyColorScheme = darkColorScheme(
    primary = NavyGold,
    onPrimary = NavyDeepBg,
    primaryContainer = NavySurfaceAlt,
    onPrimaryContainer = NavyGold,
    secondary = GoldBrassLight,
    onSecondary = NavyDeepBg,
    secondaryContainer = NavySurfaceAlt,
    onSecondaryContainer = NavyText,
    tertiary = ChancelBurgundy,
    background = NavyDeepBg,
    onBackground = NavyText,
    surface = NavySurface,
    onSurface = NavyText,
    surfaceVariant = NavySurfaceAlt,
    onSurfaceVariant = NavyTextMuted
)

// 3. Sacred Forest
val ForestColorScheme = darkColorScheme(
    primary = ForestGold,
    onPrimary = ForestDeepBg,
    primaryContainer = ForestSurfaceAlt,
    onPrimaryContainer = ForestGold,
    secondary = GoldBrassLight,
    onSecondary = ForestDeepBg,
    secondaryContainer = ForestSurfaceAlt,
    onSecondaryContainer = ForestText,
    tertiary = ForestGreen,
    background = ForestDeepBg,
    onBackground = ForestText,
    surface = ForestSurface,
    onSurface = ForestText,
    surfaceVariant = ForestSurfaceAlt,
    onSurfaceVariant = Color(0xFFA5B8AD)
)

// 4. Chancel Burgundy
val BurgundyColorScheme = darkColorScheme(
    primary = BurgundyGold,
    onPrimary = BurgundyDeepBg,
    primaryContainer = BurgundySurfaceAlt,
    onPrimaryContainer = BurgundyGold,
    secondary = GoldBrassLight,
    onSecondary = BurgundyDeepBg,
    secondaryContainer = BurgundySurfaceAlt,
    onSecondaryContainer = BurgundyText,
    tertiary = ChancelBurgundy,
    background = BurgundyDeepBg,
    onBackground = BurgundyText,
    surface = BurgundySurface,
    onSurface = BurgundyText,
    surfaceVariant = BurgundySurfaceAlt,
    onSurfaceVariant = Color(0xFFC7A8B4)
)

// 5. Dark Candlelight
val CandlelightColorScheme = darkColorScheme(
    primary = CandleAmber,
    onPrimary = Color.Black,
    primaryContainer = CandleDarkSurfaceAlt,
    onPrimaryContainer = CandleAmber,
    secondary = CandleAmber,
    onSecondary = Color.Black,
    secondaryContainer = CandleDarkSurfaceAlt,
    onSecondaryContainer = CandleDarkText,
    tertiary = GoldBrass,
    background = CandleDarkBg,
    onBackground = CandleDarkText,
    surface = CandleDarkSurface,
    onSurface = CandleDarkText,
    surfaceVariant = CandleDarkSurfaceAlt,
    onSurfaceVariant = CandleDarkMuted
)

@Composable
fun SanctuaryHymnalTheme(
    readingTheme: ReadingTheme = ReadingTheme.PARCHMENT,
    content: @Composable () -> Unit
) {
    val targetScheme = when (readingTheme) {
        ReadingTheme.PARCHMENT -> ParchmentColorScheme
        ReadingTheme.NAVY -> NavyColorScheme
        ReadingTheme.FOREST -> ForestColorScheme
        ReadingTheme.BURGUNDY -> BurgundyColorScheme
        ReadingTheme.DARK -> CandlelightColorScheme
    }

    // Smooth 200ms transition between theme modes for reverent atmosphere
    val animatedBackground = animateColorAsState(targetValue = targetScheme.background, animationSpec = tween(250), label = "bg").value
    val animatedSurface = animateColorAsState(targetValue = targetScheme.surface, animationSpec = tween(250), label = "surface").value
    val animatedOnBackground = animateColorAsState(targetValue = targetScheme.onBackground, animationSpec = tween(250), label = "onBg").value
    val animatedPrimary = animateColorAsState(targetValue = targetScheme.primary, animationSpec = tween(250), label = "primary").value

    val animatedColorScheme = targetScheme.copy(
        background = animatedBackground,
        surface = animatedSurface,
        onBackground = animatedOnBackground,
        primary = animatedPrimary
    )

    MaterialTheme(
        colorScheme = animatedColorScheme,
        typography = Typography,
        content = content
    )
}
