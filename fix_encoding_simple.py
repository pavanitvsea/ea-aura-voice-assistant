#!/usr/bin/env python3
"""
Fix character encoding issues in EA Aura HTML files
"""

# Read the file
with open('ea_aura_enhanced.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Fix the most common corrupted patterns
content = content.replace('"Š Your Wellness Dashboard', '📊 Your Wellness Dashboard')
content = content.replace('"Š', '📊')  # Dashboard/reports icon
content = content.replace('¥ Wellness', '🏥 Wellness')
content = content.replace(''° Wealth', '💰 Wealth')
content = content.replace('Ž® Games', '🎮 Games')
content = content.replace(''¡ Quote of the Day', '💡 Quote of the Day')
content = content.replace('¯ AI Insights', '🎯 AI Insights')
content = content.replace('† Recent Achievements', '🏆 Recent Achievements')
content = content.replace('š€ Launch', '🚀 Launch')
content = content.replace('¼ EA Financial', '💼 EA Financial')
content = content.replace('"ˆ Download Excel', '📈 Download Excel')
content = content.replace('ŒŸ EA Aura', '🌟 EA Aura')
content = content.replace('ª™', '🪙')  # Coin icon
content = content.replace('"–', '📖')  # Book icon
content = content.replace('"', '❓')    # Help icon

# Write back
with open('ea_aura_enhanced.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Character encoding fixes applied!")