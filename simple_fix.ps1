# Simple encoding fix script
$content = Get-Content "ea_aura_enhanced.html" -Raw -Encoding UTF8

# Replace corrupted characters one by one
$content = $content -replace "ðŸŒŸ", "🌟"
$content = $content -replace "ðŸª™", "🪙" 
$content = $content -replace "ðŸ¥", "🏥"
$content = $content -replace "ðŸ'°", "💰"
$content = $content -replace "ðŸŽ®", "🎮"
$content = $content -replace "ðŸ"Š", "📊"
$content = $content -replace "ðŸ'¡", "💡"
$content = $content -replace "ðŸŽ¯", "🎯"
$content = $content -replace "â"", "❓"

# Save back
$content | Out-File "ea_aura_enhanced.html" -Encoding UTF8
Write-Host "Fixed encoding issues!"