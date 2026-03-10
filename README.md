# EA Aura - AI Wellness Hub

**AI-Powered Wellness Platform for EA Employees**

## Quick Start

### Option 1: Static Site (GitHub Pages)
Open `index.html` in your browser - works directly without any server.

### Option 2: Streamlit Dashboard
```bash
# Install dependencies
pip install -r requirements.txt

# Generate dashboard data (REQUIRED first!)
python Hackathon_Dashboard.py

# Run dashboard
streamlit run dashboard_app.py
```
Access at: http://localhost:8501

### Option 3: Flask Backend (Full AI)
```bash
pip install -r requirements.txt
python Hackathon_Dashboard.py  # Generate data first
python app.py
```
Access at: http://localhost:5000

## Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Assistant | Health & wealth advice (Azure OpenAI / fallback) |
| 🎙️ Voice Control | Speech recognition + Male/Female/Other voices |
| 🪙 Coin Jar | Animated coins falling into jar |
| 🧮 Budget Calculator | 50/30/20 rule calculator |
| 🏦 Emergency Fund | Savings goal calculator |
| 🎮 Games | Snake, Memory, Sudoku, Zen Garden |
| 📊 KPI Dashboard | Streamlit analytics |

## Project Structure

```
EA Hackathon 2025/
├── index.html                  # Main wellness app
├── app.py                      # Flask backend
├── config_openAI.py            # Azure OpenAI config
├── dashboard_app.py            # Streamlit dashboard
├── Hackathon_Dashboard.py      # Data generator (run first!)
├── dashboard_dummy_data.xlsx   # Generated KPI data
├── requirements.txt            # Python dependencies
├── games/                      # Wellness games
├── Aura/                       # Standalone version
└── *.png                       # Character & asset images
```

## Character Images

| Character | Image | Role |
|-----------|-------|------|
| Nova | `nova_orange.png` | Habit Tracker |
| Veda | `veda_red.png` | Focus & Energy |
| Kai | `kai_blue.png` | Calm & Breath |
| Iris | `iris_green.png` | Relax & Recover |

## Environment Setup (Optional)

Create `.env` file for Azure OpenAI:
```
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

---

**EA Hackathon 2025** | Built with ❤️ for employee wellness
