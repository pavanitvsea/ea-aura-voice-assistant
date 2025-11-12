with open('ea_aura_enhanced.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix dashboard title
content = content.replace('Your Wellness Dashboard</h2>', 'Your Wellness Dashboard</h2>')
if '"Š Your Wellness Dashboard' in content:
    content = content.replace('"Š Your Wellness Dashboard', '📊 Your Wellness Dashboard')

# Fix tab labels
content = content.replace('¥ Wellness</button>', '🏥 Wellness</button>')
content = content.replace('° Wealth</button>', '💰 Wealth</button>')
content = content.replace('® Games</button>', '🎮 Games</button>')

with open('ea_aura_enhanced.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed encoding issues!")