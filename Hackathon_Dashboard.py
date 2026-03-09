"""
EA Aura Dashboard Data Generator
Generates realistic wellness KPI data for the EA Aura dashboard.
"""
import pandas as pd
from datetime import datetime, timedelta
import random
import numpy as np
from pathlib import Path

# Configuration
np.random.seed(42)
random.seed(42)

# Character/Feature names for the wellness assistants
FEATURE_NAMES = ['Nova', 'Kai', 'Veda', 'Iris']

# Output paths
DATA_DIR = Path(__file__).parent
OUTPUT_FILE = DATA_DIR / 'dashboard_dummy_data.xlsx'


def generate_wellness_data(days: int = 30, start_date: datetime = None) -> pd.DataFrame:
    """
    Generate realistic wellness KPI data with positive growth trends.
    
    Args:
        days: Number of days of data to generate
        start_date: Starting date for the data (defaults to 30 days ago)
    
    Returns:
        DataFrame with wellness metrics
    """
    if start_date is None:
        start_date = datetime.now() - timedelta(days=days)
    
    data = {
        'Date': [start_date + timedelta(days=i) for i in range(days)],
        
        # User metrics with growth trends
        'Daily Active Users': [int(3000 + i * 150 + random.randint(-100, 100)) for i in range(days)],
        'Monthly Active Users': [int(28000 + i * 200 + random.randint(-100, 100)) for i in range(days)],
        'Total Users': [int(50000 + i * 300 + random.randint(-200, 200)) for i in range(days)],
        
        # Voice feature adoption
        'Users Adopting Voice Features': [int(8000 + i * 250 + random.randint(-100, 100)) for i in range(days)],
        
        # Feedback metrics
        'Total Feedback Responses': [random.randint(800, 1200) for _ in range(days)],
        'Satisfied Responses': [random.randint(700, 1100) for _ in range(days)],
        
        # User interaction metrics
        'User ID': [f'USER_{1000+i}' for i in range(days)],
        'Character Interacted': [random.randint(1, 50) for _ in range(days)],
        'Interaction Count': [random.randint(150, 500) for _ in range(days)],
        
        # Session metrics
        'Session ID': [f'SESSION_{5000+i}' for i in range(days)],
        'Duration (minutes)': [random.randint(20, 120) for _ in range(days)],
        'Total Sessions': [random.randint(500, 1500) for _ in range(days)],
        'Sessions with Voice Interaction': [random.randint(300, 1000) for _ in range(days)],
        
        # Retention metrics
        'New Users (Day 0)': [random.randint(150, 300) for _ in range(days)],
        'Retained Users (Day 30)': [random.randint(120, 250) for _ in range(days)],
        
        # Rating metrics
        'Number of Ratings': [random.randint(300, 800) for _ in range(days)],
        'Average Rating': [round(random.uniform(4.2, 4.9), 2) for _ in range(days)],
        
        # Feature tracking
        'Feature Name': [FEATURE_NAMES[i % len(FEATURE_NAMES)] for i in range(days)],
        'Planned Start Date': [start_date + timedelta(days=15 + i*2) for i in range(days)],
        'Planned End Date': [start_date + timedelta(days=20 + i*2) for i in range(days)],
        'Current Progress': [min(100, 30 + i * 2 + random.randint(-5, 5)) for i in range(days)]
    }
    
    df = pd.DataFrame(data)
    
    # Ensure data consistency
    for idx in df.index:
        if df.loc[idx, 'Satisfied Responses'] > df.loc[idx, 'Total Feedback Responses']:
            df.loc[idx, 'Satisfied Responses'] = df.loc[idx, 'Total Feedback Responses']
        
        if df.loc[idx, 'Retained Users (Day 30)'] > df.loc[idx, 'New Users (Day 0)']:
            df.loc[idx, 'Retained Users (Day 30)'] = df.loc[idx, 'New Users (Day 0)']
    
    return df


def calculate_kpi_summary(df: pd.DataFrame) -> dict:
    """Calculate key performance indicators from the data."""
    return {
        'dau_range': (df['Daily Active Users'].min(), df['Daily Active Users'].max()),
        'mau_range': (df['Monthly Active Users'].min(), df['Monthly Active Users'].max()),
        'satisfaction_rate': df['Satisfied Responses'].sum() / df['Total Feedback Responses'].sum() * 100,
        'voice_adoption_rate': df['Users Adopting Voice Features'].sum() / df['Total Users'].sum() * 100,
        'avg_rating': df['Average Rating'].mean(),
        'retention_rate': df['Retained Users (Day 30)'].sum() / df['New Users (Day 0)'].sum() * 100,
        'unique_features': list(df['Feature Name'].unique())
    }


def export_to_excel(df: pd.DataFrame, filepath: Path = OUTPUT_FILE) -> None:
    """Export DataFrame to Excel file."""
    df.to_excel(filepath, index=False, sheet_name='Dashboard Data')
    print(f"Data exported to: {filepath}")


def print_summary(df: pd.DataFrame) -> None:
    """Print a summary of the generated data."""
    kpi = calculate_kpi_summary(df)
    
    print("\n" + "=" * 60)
    print("EA Aura Dashboard Data Generator - Summary")
    print("=" * 60)
    print(f"\nData Preview:\n{df.head(5)}")
    print(f"\nWellness Assistant Characters: {', '.join(FEATURE_NAMES)}")
    print(f"\nKey Metrics Summary:")
    print(f"  DAU Range: {kpi['dau_range'][0]:,} - {kpi['dau_range'][1]:,}")
    print(f"  MAU Range: {kpi['mau_range'][0]:,} - {kpi['mau_range'][1]:,}")
    print(f"  Satisfaction Rate: {kpi['satisfaction_rate']:.1f}%")
    print(f"  Voice Adoption: {kpi['voice_adoption_rate']:.1f}%")
    print(f"  Average Rating: {kpi['avg_rating']:.2f} stars")
    print(f"  Retention Rate: {kpi['retention_rate']:.1f}%")
    print("=" * 60)


def main():
    """Main function to generate and export wellness data."""
    print("Generating EA Aura wellness dashboard data...")
    
    df = generate_wellness_data(days=30)
    
    export_to_excel(df)
    
    print_summary(df)
    
    return df


if __name__ == "__main__":
    main()
