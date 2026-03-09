"""
EA Aura Wellness Hub - Flask Backend Application
Serves the wellness dashboard and provides AI assistant API endpoints.
"""
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from pathlib import Path

from config_openAI import get_aura_response

app = Flask(__name__, static_folder='.', template_folder='.')
CORS(app)

conversation_histories = {}


@app.route('/')
def index():
    """Serve the main landing page."""
    return send_from_directory('.', 'index.html')


@app.route('/aura')
def aura_app():
    """Serve the EA Aura Enhanced wellness application."""
    return send_from_directory('.', 'ea_aura_enhanced.html')


@app.route('/games/<path:filename>')
def serve_games(filename):
    """Serve game files from the games directory."""
    return send_from_directory('games', filename)


@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, images, etc.)."""
    return send_from_directory('.', filename)


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    AI Chat endpoint for Aura assistant.
    Accepts JSON with 'message' and optional 'session_id' for conversation context.
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'success': False,
                'error': 'No message provided'
            }), 400
        
        user_message = data['message']
        session_id = data.get('session_id', 'default')
        character = data.get('character', 'nova')
        
        if session_id not in conversation_histories:
            conversation_histories[session_id] = []
        
        history = conversation_histories[session_id]
        
        character_context = get_character_context(character)
        full_message = f"[Character: {character}] {user_message}" if character else user_message
        
        response = get_aura_response(full_message, history)
        
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": response})
        
        if len(history) > 20:
            conversation_histories[session_id] = history[-20:]
        
        return jsonify({
            'success': True,
            'response': response,
            'character': character
        })
        
    except Exception as e:
        print(f"Chat API Error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/chat/clear', methods=['POST'])
def clear_chat():
    """Clear conversation history for a session."""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        
        if session_id in conversation_histories:
            del conversation_histories[session_id]
        
        return jsonify({
            'success': True,
            'message': 'Conversation history cleared'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/wellness/tips', methods=['GET'])
def get_wellness_tips():
    """Get daily wellness tips based on category."""
    category = request.args.get('category', 'general')
    
    tips = {
        'physical': [
            "🏃 Take a 5-minute walk every hour to boost circulation and energy",
            "💧 Drink a glass of water right now - hydration improves focus by 25%",
            "🧘 Do 3 desk stretches: neck rolls, shoulder shrugs, wrist circles"
        ],
        'mental': [
            "🧠 Practice the 4-7-8 breathing technique for instant calm",
            "📝 Write down 3 things you're grateful for today",
            "🎧 Listen to calming music for 5 minutes to reset your mind"
        ],
        'productivity': [
            "🎯 Use the Pomodoro Technique: 25 min work, 5 min break",
            "📋 Write your top 3 priorities for today",
            "🚫 Turn off notifications for 1 hour of deep work"
        ],
        'social': [
            "👋 Reach out to a colleague you haven't spoken to recently",
            "☕ Schedule a virtual coffee chat with a team member",
            "🙏 Send a thank you message to someone who helped you"
        ],
        'purpose': [
            "🎯 Reflect on one achievement you're proud of this week",
            "📈 Set one small goal that aligns with your long-term vision",
            "💡 Learn something new for 10 minutes today"
        ],
        'general': [
            "✨ Take 3 deep breaths and smile - it releases endorphins!",
            "🌿 Step outside for fresh air and natural light",
            "🎮 Playing wellness games can improve focus and reduce stress"
        ]
    }
    
    import random
    category_tips = tips.get(category, tips['general'])
    
    return jsonify({
        'success': True,
        'category': category,
        'tips': category_tips,
        'featured_tip': random.choice(category_tips)
    })


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'EA Aura Wellness Hub',
        'version': '1.0.0'
    })


def get_character_context(character: str) -> str:
    """Get personality context for different Aura characters."""
    characters = {
        'nova': "You are Nova, the habit tracking companion. You're energetic, encouraging, and focused on building consistent wellness routines. Use 🏃‍♀️ emoji occasionally.",
        'veda': "You are Veda, the focus and energy coach. You're motivating, driven, and help boost productivity. Use 💪 emoji occasionally.",
        'kai': "You are Kai, the calm and breath guide. You're peaceful, zen-like, and help with mindfulness and stress management. Use 🧘‍♂️ emoji occasionally.",
        'iris': "You are Iris, the relaxation and recovery specialist. You're gentle, nurturing, and focused on rest and healing. Use 🌿 emoji occasionally."
    }
    return characters.get(character, characters['nova'])


if __name__ == '__main__':
    print("=" * 50)
    print("🌟 EA Aura Wellness Hub Starting...")
    print("=" * 50)
    print("\n📍 Access the application at:")
    print("   - Landing Page: http://localhost:5000/")
    print("   - Aura App: http://localhost:5000/aura")
    print("   - API Health: http://localhost:5000/api/health")
    print("\n💡 Press Ctrl+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
