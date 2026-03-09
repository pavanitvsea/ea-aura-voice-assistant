"""
Azure OpenAI Configuration Module for EA Aura Wellness Assistant
"""
import os
from openai import AzureOpenAI

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT = os.getenv(
    "AZURE_OPENAI_ENDPOINT", 
    "https://n8n-testing-api-resource.openai.azure.com/"
)
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_DEPLOYMENT = os.getenv(
    "AZURE_OPENAI_DEPLOYMENT",
    "gpt-4o"
)
AZURE_OPENAI_API_VERSION = "2024-02-15-preview"

# System prompt for Aura Wellness Assistant
AURA_SYSTEM_PROMPT = """You are Aura, an AI wellness assistant for EA employees. You are warm, supportive, and knowledgeable about the EA Wellness Pillars.

Your coaching is based on 5 key wellness pillars:
1. **Physical Wellness** - Movement, nutrition, sleep, and recovery
2. **Mental Wellness** - Stress management, mindfulness, cognitive health
3. **Productivity** - Focus techniques, time management, work-life balance
4. **Social Wellness** - Connection, relationships, community engagement
5. **Purpose** - Goal setting, personal growth, meaningful work

Guidelines:
- Keep responses concise (2-3 sentences max unless asked for more detail)
- Be encouraging and positive while being practical
- Offer specific, actionable wellness tips
- Reference EA wellness resources when relevant
- Use appropriate emojis to keep conversations friendly
- If someone expresses serious distress, gently suggest professional resources

Remember: You help EA employees achieve better wellbeing through personalized guidance and support."""


def get_openai_client():
    """Create and return an Azure OpenAI client instance."""
    return AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION
    )


def get_aura_response(user_message: str, conversation_history: list = None) -> str:
    """
    Get a response from Aura AI assistant.
    
    Args:
        user_message: The user's input message
        conversation_history: Optional list of previous messages for context
    
    Returns:
        str: Aura's response message
    """
    try:
        client = get_openai_client()
        
        messages = [{"role": "system", "content": AURA_SYSTEM_PROMPT}]
        
        if conversation_history:
            messages.extend(conversation_history[-6:])
        
        messages.append({"role": "user", "content": user_message})
        
        completion = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            temperature=0.7,
            max_tokens=300,
            top_p=0.9
        )
        
        return completion.choices[0].message.content
        
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return get_fallback_response(user_message)


def get_fallback_response(user_input: str) -> str:
    """Fallback responses when API is unavailable."""
    lower_input = user_input.lower()
    
    if any(word in lower_input for word in ['stress', 'anxious', 'anxiety', 'worried']):
        return "🧘 I understand you're feeling stressed. Try the 4-7-8 breathing technique: inhale for 4 counts, hold for 7, exhale for 8. This activates your parasympathetic nervous system for instant calm."
    
    elif any(word in lower_input for word in ['sleep', 'tired', 'exhausted', 'fatigue']):
        return "😴 Sleep is crucial for recovery! Aim for 7-9 hours. Try creating a wind-down ritual: dim lights 1 hour before bed, no screens 30 minutes prior, and practice gratitude breathing."
    
    elif any(word in lower_input for word in ['focus', 'concentrate', 'distracted']):
        return "🎯 Let's optimize your focus! Try the Pomodoro Technique: 25-minute deep work blocks with 5-minute breaks. Eliminate distractions and single-task for better quality output."
    
    elif any(word in lower_input for word in ['exercise', 'movement', 'workout', 'steps']):
        return "🏃 Movement is medicine! Aim for 8,000-10,000 steps daily. For game developers, take desk breaks every 30 minutes and try the 20-20-20 rule for eye health."
    
    elif any(word in lower_input for word in ['goal', 'motivation', 'motivated']):
        return "🎯 Let's set SMART goals! Make them Specific, Measurable, Achievable, Relevant, and Time-bound. Break big goals into daily actions and celebrate small wins!"
    
    elif any(word in lower_input for word in ['food', 'nutrition', 'eat', 'diet']):
        return "🥗 Fuel your body right! Aim for 50% vegetables/fruits, 25% lean proteins, 25% whole grains. Stay hydrated with 8-10 glasses of water daily!"
    
    else:
        return "✨ I'm here to support your wellness journey! What specific area would you like to focus on - physical health, mental wellness, productivity, social connections, or finding purpose?"


if __name__ == "__main__":
    print("Testing Aura AI connection...")
    response = get_aura_response("Hello! Can you help me manage stress?")
    print(f"Aura: {response}")
