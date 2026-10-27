package com.pnba.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.gestures.detectDragGestures
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.layout.onGloballyPositioned
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun StickyScrubber(
    letters: List<Char>,
    onLetterSelected: (Char) -> Unit,
    modifier: Modifier = Modifier
) {
    var columnHeight by remember { mutableIntStateOf(1) }
    var activeChar by remember { mutableStateOf<Char?>(null) }

    Box(
        modifier = modifier
            .width(28.dp)
            .clip(RoundedCornerShape(14.dp))
            .background(MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f))
            .padding(vertical = 4.dp)
            .onGloballyPositioned { coordinates ->
                columnHeight = coordinates.size.height
            }
            .pointerInput(letters, columnHeight) {
                detectTapGestures { offset ->
                    val index = ((offset.y / columnHeight) * letters.size).toInt().coerceIn(0, letters.size - 1)
                    val letter = letters[index]
                    activeChar = letter
                    onLetterSelected(letter)
                }
            }
            .pointerInput(letters, columnHeight) {
                detectDragGestures(
                    onDragStart = { offset ->
                        val index = ((offset.y / columnHeight) * letters.size).toInt().coerceIn(0, letters.size - 1)
                        val letter = letters[index]
                        activeChar = letter
                        onLetterSelected(letter)
                    },
                    onDragEnd = { activeChar = null },
                    onDragCancel = { activeChar = null },
                    onDrag = { change, _ ->
                        change.consume()
                        val y = change.position.y
                        val index = ((y / columnHeight) * letters.size).toInt().coerceIn(0, letters.size - 1)
                        val letter = letters[index]
                        if (letter != activeChar) {
                            activeChar = letter
                            onLetterSelected(letter)
                        }
                    }
                )
            }
            .testTag("alphabetical_scrubber"),
        contentAlignment = Alignment.Center
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            for (char in letters) {
                val isSelected = activeChar == char
                Text(
                    text = char.toString(),
                    fontSize = 10.sp,
                    fontWeight = if (isSelected) FontWeight.ExtraBold else FontWeight.Medium,
                    color = if (isSelected) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(vertical = 1.dp)
                )
            }
        }
    }
}
