# EA Aura - AI Wellness Hub

**AI-Powered Wellness Platform for EA Employees**

## Quick Start

### Run the Wellness App (Static - GitHub Pages)
Open `index.html` in your browser - works directly without any server.

### Run Streamlit Dashboard
```bash
pip install -r requirements.txt
python Hackathon_Dashboard.py  # Generate data
streamlit run dashboard_app.py
```
Access at: http://localhost:8501

### Run Flask Backend (Optional - for full AI)
```bash
pip install -r requirements.txt
python app.py
```
Access at: http://localhost:5000

## Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Assistant | Health & wealth advice powered by Azure OpenAI |
| 🎙️ Voice Control | Speech recognition and text-to-speech |
| 🧮 Budget Calculator | 50/30/20 rule with instant calculations |
| 🏦 Emergency Fund | Goal calculator for financial security |
| 🎮 Game Hub | Cognitive wellness games |
| 📊 KPI Dashboard | Streamlit analytics with interactive charts |

## Project Structure

```
EA Hackathon 2025/
├── index.html              # Main wellness app (all-in-one)
├── app.py                  # Flask backend (optional)
├── config_openAI.py        # Azure OpenAI configuration
├── dashboard_app.py        # Streamlit KPI dashboard
├── Hackathon_Dashboard.py  # Data generator
├── requirements.txt        # Python dependencies
├── games/                  # Wellness games
│   └── index.html          # Game Hub
└── dashboard_dummy_data.xlsx
```

## Environment Setup (Optional)

Create `.env` file for Azure OpenAI:
```
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

## Live Demo

GitHub Pages: The `index.html` works as a standalone static site with smart AI fallback responses.

---

**EA Hackathon 2025** | Built with ❤️ for employee wellness
