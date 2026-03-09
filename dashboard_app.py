import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="EA Aura KPI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    try:
        data_path = Path(__file__).parent / 'dashboard_dummy_data.xlsx'
        df = pd.read_excel(data_path)
        df = df.sort_values('Date').reset_index(drop=True)
        df['Daily Active Users'] = df['Daily Active Users'] * (1 + np.arange(len(df)) * 0.02)
        return df.astype({'Daily Active Users': 'int64'})
    except Exception as e:
        st.error(f"Error loading data: {e}. Run `python Hackathon_Dashboard.py` first to generate data.")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# Sidebar Filters
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("---")

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df['Date'].min().date(), df['Date'].max().date()),
    key="date_range"
)

if len(date_range) == 2:
    df_filtered = df[(df['Date'].dt.date >= date_range[0]) & (df['Date'].dt.date <= date_range[1])]
else:
    df_filtered = df

# Header
st.markdown("""
<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
    <div style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 12px 20px; border-radius: 12px;">
        <span style="font-size: 1.5em;">📊</span>
    </div>
    <div>
        <h1 style="margin: 0; color: #333;">EA Aura KPI Dashboard</h1>
        <p style="margin: 0; color: #666;">Real-time wellness metrics and insights</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Calculate metrics
avg_dau = df_filtered['Daily Active Users'].mean() if len(df_filtered) > 0 else 0
dau_change = ((df_filtered['Daily Active Users'].iloc[-1] - df_filtered['Daily Active Users'].iloc[0]) / df_filtered['Daily Active Users'].iloc[0] * 100) if len(df_filtered) > 1 else 0
avg_mau = df_filtered['Monthly Active Users'].mean() if 'Monthly Active Users' in df_filtered.columns else 0
satisfaction_rate = (df_filtered['Satisfied Responses'].sum() / df_filtered['Total Feedback Responses'].sum() * 100) if df_filtered['Total Feedback Responses'].sum() > 0 else 0
voice_adoption = (df_filtered['Users Adopting Voice Features'].mean() / df_filtered['Total Users'].mean() * 100) if df_filtered['Total Users'].mean() > 0 else 0
avg_rating = df_filtered['Average Rating'].mean() if 'Average Rating' in df_filtered.columns else 0

# KPI Cards Row
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Avg Daily Users", f"{int(avg_dau):,}", f"{dau_change:+.1f}%")

with col2:
    st.metric("Avg Monthly Users", f"{int(avg_mau):,}")

with col3:
    st.metric("Satisfaction", f"{satisfaction_rate:.1f}%", "Excellent" if satisfaction_rate > 80 else "Good")

with col4:
    st.metric("Voice Adoption", f"{voice_adoption:.1f}%")

with col5:
    st.metric("Avg Rating", f"{avg_rating:.2f}⭐")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "👥 User Metrics", "💬 Feedback", "📚 About"])

with tab1:
    st.subheader("Performance Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.area(df_filtered, x='Date', y='Daily Active Users',
                      title='Daily Active Users',
                      color_discrete_sequence=['#667eea'])
        fig1.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.area(df_filtered, x='Date', y='Monthly Active Users',
                      title='Monthly Active Users',
                      color_discrete_sequence=['#764ba2'])
        fig2.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig3 = px.line(df_filtered, x='Date',
                      y=['Total Sessions', 'Sessions with Voice Interaction'],
                      title='Session Activity', markers=True)
        fig3.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        df_copy = df_filtered.copy()
        df_copy['Duration_Bucket'] = pd.cut(df_copy['Duration (minutes)'],
                                           bins=[0, 30, 60, 120],
                                           labels=['0-30min', '30-60min', '60+min'])
        duration_count = df_copy['Duration_Bucket'].value_counts()
        fig4 = go.Figure(data=[
            go.Bar(x=duration_count.index, y=duration_count.values,
                  marker_color=['#667eea', '#764ba2', '#f093fb'])
        ])
        fig4.update_layout(title='Session Duration', height=400, template='plotly_white')
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    st.subheader("User Engagement")
    
    col1, col2 = st.columns(2)
    
    with col1:
        retention_data = df_filtered[['New Users (Day 0)', 'Retained Users (Day 30)']].mean()
        retention_pct = (retention_data['Retained Users (Day 30)'] / retention_data['New Users (Day 0)'] * 100)
        
        fig5 = go.Figure(data=[
            go.Funnel(
                y=['New Users', 'Retained (30 days)'],
                x=[retention_data['New Users (Day 0)'], retention_data['Retained Users (Day 30)']],
                marker=dict(color=['#667eea', '#764ba2'])
            )
        ])
        fig5.update_layout(title=f'Retention Funnel ({retention_pct:.1f}%)', height=400, template='plotly_white')
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        fig6 = px.histogram(df_filtered, x='Interaction Count', nbins=20,
                           title='Interaction Distribution',
                           color_discrete_sequence=['#764ba2'])
        fig6.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig6, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Character Interacted' in df_filtered.columns:
            fig7 = px.bar(df_filtered, x='Character Interacted', y='Interaction Count',
                         title='Character Interactions',
                         color='Interaction Count', color_continuous_scale='Purples')
            fig7.update_layout(height=400, template='plotly_white')
            st.plotly_chart(fig7, use_container_width=True)
    
    with col2:
        voice_trend = df_filtered.copy()
        voice_trend['Voice_Pct'] = (voice_trend['Users Adopting Voice Features'] / voice_trend['Total Users'] * 100)
        fig8 = px.area(voice_trend, x='Date', y='Voice_Pct',
                      title='Voice Feature Adoption %',
                      color_discrete_sequence=['#f093fb'])
        fig8.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig8, use_container_width=True)

with tab3:
    st.subheader("Feedback & Ratings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig9 = px.bar(df_filtered, x='Date',
                     y=['Total Feedback Responses', 'Satisfied Responses'],
                     title='Feedback Responses', barmode='group')
        fig9.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig9, use_container_width=True)
    
    with col2:
        fig10 = go.Figure(data=[go.Indicator(
            mode="gauge+number",
            value=satisfaction_rate,
            title={'text': "Satisfaction Rate (%)"},
            gauge={'axis': {'range': [0, 100]},
                  'bar': {'color': "#667eea"},
                  'steps': [
                      {'range': [0, 50], 'color': "#ffcccb"},
                      {'range': [50, 80], 'color': "#fffacd"},
                      {'range': [80, 100], 'color': "#90EE90"}],
                  'threshold': {
                      'line': {'color': "green", 'width': 4},
                      'thickness': 0.75,
                      'value': 85}}
        )])
        fig10.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig10, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig11 = px.histogram(df_filtered, x='Average Rating', nbins=10,
                            title='Rating Distribution',
                            color_discrete_sequence=['#667eea'])
        fig11.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig11, use_container_width=True)
    
    with col2:
        fig12 = px.scatter(df_filtered, x='Number of Ratings', y='Average Rating',
                          size='Interaction Count', title='Ratings vs Interactions',
                          color='Average Rating', color_continuous_scale='Purples')
        fig12.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig12, use_container_width=True)

with tab4:
    st.subheader("About EA Aura")
    
    st.markdown("""
    ### EA Aura Wellness Platform
    
    EA Aura is an AI-powered wellness hub for EA employees featuring:
    
    - **AI Wellness Coach** - Personalized health and wealth advice
    - **Voice Controls** - Hands-free interaction with speech recognition
    - **Gamification** - Earn coins for healthy habits
    - **Wellness Games** - Cognitive training games
    - **Financial Tools** - Budget calculator, emergency fund planner
    
    ### Dashboard Metrics
    
    | Metric | Description |
    |--------|-------------|
    | DAU | Daily Active Users |
    | MAU | Monthly Active Users |
    | Satisfaction | % of positive feedback |
    | Voice Adoption | % using voice features |
    | Avg Rating | User satisfaction score |
    
    ### How to Use
    
    1. Use the sidebar to filter by date range
    2. Explore tabs for different metric views
    3. Export data using the button below
    """)
    
    st.markdown("---")
    st.info(f"Dashboard updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Data Export
st.markdown("---")
with st.expander("📥 Export Data"):
    st.dataframe(df_filtered, use_container_width=True)
    csv = df_filtered.to_csv(index=False)
    st.download_button("Download CSV", csv, "ea_aura_kpi_data.csv", "text/csv")
