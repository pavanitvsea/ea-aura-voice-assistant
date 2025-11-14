import pandas as pd
from datetime import datetime, timedelta
import random
import numpy as np

# Generate dummy data with ALL POSITIVE METRICS
np.random.seed(42)
random.seed(42)

# Feature names mapping
feature_names = ['Nova', 'Kai', 'Veda', 'Iris', 'Nova']  # Removed Feature_0, using rotation of existing names

data = {
    'Date': [datetime(2025, 11, 1) + timedelta(days=i) for i in range(30)],
    'Daily Active Users': [int(3000 + i * 150 + random.randint(-100, 100)) for i in range(30)],  # Growing trend
    'Monthly Active Users': [int(28000 + i * 200 + random.randint(-100, 100)) for i in range(30)],  # Growing trend
    'Total Feedback Responses': [random.randint(800, 1200) for _ in range(30)],
    'Satisfied Responses': [random.randint(700, 1100) for _ in range(30)],
    'Total Users': [int(50000 + i * 300 + random.randint(-200, 200)) for i in range(30)],  # Growing
    'Users Adopting Voice Features': [int(8000 + i * 250 + random.randint(-100, 100)) for i in range(30)],  # Growing
    'User ID': [f'USER_{1000+i}' for i in range(30)],
    'Character Interacted': [random.randint(1, 50) for _ in range(30)],
    'Interaction Count': [random.randint(150, 500) for _ in range(30)],
    'Session ID': [f'SESSION_{5000+i}' for i in range(30)],
    'Duration (minutes)': [random.randint(20, 120) for _ in range(30)],
    'Total Sessions': [random.randint(500, 1500) for _ in range(30)],
    'Sessions with Voice Interaction': [random.randint(300, 1000) for _ in range(30)],
    'New Users (Day 0)': [random.randint(150, 300) for _ in range(30)],
    'Retained Users (Day 30)': [random.randint(120, 250) for _ in range(30)],
    'Number of Ratings': [random.randint(300, 800) for _ in range(30)],
    'Average Rating': [round(random.uniform(4.2, 4.9), 2) for _ in range(30)],
    'Feature Name': [feature_names[i % 4] for i in range(30)],  # Cycle through Nova, Kai, Veda, Iris
    'Planned Start Date': [datetime(2025, 11, 15) + timedelta(days=i*2) for i in range(30)],
    'Planned End Date': [datetime(2025, 11, 20) + timedelta(days=i*2) for i in range(30)],
    'Current Progress': [min(100, 30 + i * 2 + random.randint(-5, 5)) for i in range(30)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Ensure satisfied responses <= total responses
for idx in df.index:
    if df.loc[idx, 'Satisfied Responses'] > df.loc[idx, 'Total Feedback Responses']:
        df.loc[idx, 'Satisfied Responses'] = df.loc[idx, 'Total Feedback Responses']

# Ensure retained <= new users
for idx in df.index:
    if df.loc[idx, 'Retained Users (Day 30)'] > df.loc[idx, 'New Users (Day 0)']:
        df.loc[idx, 'Retained Users (Day 30)'] = df.loc[idx, 'New Users (Day 0)']

# Export to Excel
OUTPUT_PATH = r'C:\Users\akoujalagi\OneDrive - Electronic Arts\Desktop\Py dashboard\dashboard_dummy_data.xlsx'
df.to_excel(OUTPUT_PATH, index=False, sheet_name='Dashboard Data')
print("✅ Excel file created successfully!")
print(OUTPUT_PATH)
print(f"\n📊 Data Preview:\n{df.head(10)}")
print(f"\n✨ Feature Names Updated:")
print(f"   • Feature_0 → REMOVED (replaced with Nova, Kai, Veda, Iris)")
print(f"   • Feature_1 → Nova ✨")
print(f"   • Feature_2 → Kai ✨")
print(f"   • Feature_3 → Veda ✨")
print(f"   • Feature_4 → Iris ✨")
print(f"\n📈 Key Metrics Summary:")
print(f"   • DAU Range: {df['Daily Active Users'].min()} - {df['Daily Active Users'].max()} ✅ GROWING")
print(f"   • MAU Range: {df['Monthly Active Users'].min()} - {df['Monthly Active Users'].max()} ✅ GROWING")
print(f"   • Avg Satisfaction: {(df['Satisfied Responses'].sum() / df['Total Feedback Responses'].sum() * 100):.1f}% ✅ EXCELLENT")
print(f"   • Voice Adoption: {(df['Users Adopting Voice Features'].sum() / df['Total Users'].sum() * 100):.1f}% ✅ GROWING")
print(f"   • Avg Rating: {df['Average Rating'].mean():.2f}⭐ ✅ EXCELLENT")
print(f"\n📊 Unique Features:")
print(f"   {df['Feature Name'].unique()}")