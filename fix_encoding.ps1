# Fix emoji encoding issues in EA Aura HTML files
Write-Host "Fixing emoji encoding issues..."

$content = Get-Content "ea_aura_enhanced.html" -Raw -Encoding UTF8

# Replace corrupted emojis with proper UTF-8 versions one by one
$content = $content -replace "ðŸŒŸ", "🌟"
$content = $content -replace "ðŸª™", "🪙" 
$content = $content -replace "ðŸ¥", "🏥"
$content = $content -replace "ðŸ'°", "💰"
$content = $content -replace "ðŸŽ®", "🎮"
$content = $content -replace "ðŸ"Š", "📊"
$content = $content -replace "ðŸ'¡", "💡"
$content = $content -replace "ðŸŽ¯", "🎯"
$content = $content -replace "ðŸ'¼", "💼"
$content = $content -replace "ðŸ"ˆ", "📈"
$content = $content -replace "ðŸ§¾", "🧾"
$content = $content -replace "ðŸš€", "🚀"
$content = $content -replace "ðŸ†", "🏆"
$content = $content -replace "ðŸ"–", "📖"
$content = $content -replace "ðŸƒ", "🧠"
$content = $content -replace "ðŸ"¢", "🔢"
$content = $content -replace "ðŸ§©", "🧩"
$content = $content -replace "ðŸŒŠ", "🌊"
$content = $content -replace "ðŸŽ²", "🎲"
$content = $content -replace "â"", "❓"
$content = $content -replace "âœ…", "✅"
$content = $content -replace "Ã—", "×"

# Save the fixed content
$content | Set-Content "ea_aura_enhanced.html" -Encoding UTF8

Write-Host "Emoji encoding fixed!"