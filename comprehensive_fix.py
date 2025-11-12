#!/usr/bin/env python3
"""
Complete character encoding fix for EA Aura HTML files
"""

def fix_encoding():
    # Read the file
    with open('ea_aura_enhanced.html', 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    print("🔧 Starting comprehensive encoding fixes...")
    
    # Tab navigation fixes
    print("📑 Fixing tab navigation...")
    content = content.replace("'💰 Wealth</button>", "💰 Wealth</button>")
    content = content.replace("> Wealth</button>", "💰 Wealth</button>")
    content = content.replace("> Games</button>", "🎮 Games</button>")  
    content = content.replace("> Reports</button>", "📊 Reports</button>")
    
    # Fix duplicated wealth tabs
    lines = content.split('\n')
    cleaned_lines = []
    wealth_button_found = False
    
    for line in lines:
        if 'switchTab(\'wealth\')' in line and 'Wealth</button>' in line:
            if not wealth_button_found:
                # Keep only the first properly formatted wealth button
                cleaned_lines.append('                <button class="tab-btn" onclick="switchTab(\'wealth\')">💰 Wealth</button>')
                wealth_button_found = True
        elif 'switchTab(\'games\')' in line:
            cleaned_lines.append('                <button class="tab-btn" onclick="switchTab(\'games\')">🎮 Games</button>')
        elif 'switchTab(\'reports\')' in line:
            cleaned_lines.append('                <button class="tab-btn" onclick="switchTab(\'reports\')">📊 Reports</button>')
        elif '</div>' in line and len(cleaned_lines) > 0 and 'tab-navigation' in cleaned_lines[-5:][0] if len(cleaned_lines) >= 5 else False:
            # Add missing help button before closing div of tab-navigation
            if not any('help' in prev_line for prev_line in cleaned_lines[-5:]):
                cleaned_lines.append('                <button class="tab-btn" onclick="switchTab(\'help\')">❓ Help</button>')
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    
    content = '\n'.join(cleaned_lines)
    
    # Additional character fixes
    print("✨ Fixing remaining corrupted characters...")
    fixes = [
        ("'¡ Quote", "💡 Quote"),
        ("¯ AI", "🎯 AI"),
        ("† Recent", "🏆 Recent"),
        ("š€ Launch", "🚀 Launch"),
        ("¼ EA", "💼 EA"),
        (""ˆ Download", "📈 Download"),
        ("ŒŸ EA", "🌟 EA"),
        ("'°", "💰"),
        ("®", "🎮"),
        (""Š", "📊"),
        ("¥", "🏥"),
        (""", "❓"),
    ]
    
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
            print(f"  ✅ Fixed: {old} → {new}")
    
    # Write back
    with open('ea_aura_enhanced.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("🎉 Character encoding fixes completed!")
    print("📊 Tab navigation cleaned and proper emojis restored")

if __name__ == "__main__":
    fix_encoding()