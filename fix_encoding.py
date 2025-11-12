#!/usr/bin/env python3
"""
Fix character encoding issues in EA Aura HTML files
"""

# Read the file with proper encoding handling
with open('ea_aura_enhanced.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Define replacements for corrupted characters
replacements = {
    '"Š': '📊',  # Dashboard icon
    '¥': '🏥',   # Wellness tab
    ''°': '💰',  # Wealth tab  
    'Ž®': '🎮',  # Games tab
    ''¡': '💡',  # Quote icon
    '¯': '🎯',   # AI insights icon
    '†': '🏆',   # Achievements
    'š€': '🚀',  # Launch icon
    '¼': '💼',   # Business icon
    '"ˆ': '📈',  # Chart icon
    'ŒŸ': '🌟',  # Star icon
    'ª™': '🪙',  # Coin icon
    '"–': '📖',  # Book icon
    '§¾': '🧾',  # Receipt icon
    '"': '❓',   # Question mark
    '✅': '✅',  # Checkmark (keep as is)
    '×': '×',    # Close button (keep as is)
}

# Apply replacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Additional fixes for specific patterns
content = content.replace('ðŸ', '🏥')  # Fix any remaining wellness icons
content = content.replace('ð', '')     # Remove orphaned characters

# Write back with UTF-8 encoding
with open('ea_aura_enhanced.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Character encoding fixes applied successfully!")
print("🔧 Fixed corrupted emojis and special characters")