from google import genai
from google.genai import types
from dotenv import load_dotenv
from datetime import datetime

GEMINI_MODEL = "gemini-2.5-flash"

# Load GEMINI_API_KEY environment variable
load_dotenv()

client = genai.Client()

# Display welcome banner
print("\n" + "=" * 60)
print("✓ GEMINI CHATBOT".center(60))
print("=" * 60)
print("Type 'endchat' to exit the conversation.\n")

conversation_history = []
message_count = 0

# Get initial user input
user_input = input("You: ").strip()

while user_input.lower() != "endchat":
    if not user_input:
        print("⚠ Please enter a message.\n")
        user_input = input("You: ").strip()
        continue

    message_count += 1
    
    # Add user message to history as string
    conversation_history.append(f"User: {user_input}")

    try:
        # Get chatbot response
        chatbot_response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents="\n".join(conversation_history),
            config=types.GenerateContentConfig(
                system_instruction="Answer in 1 line, within 50 words.",
                temperature=0.1,
            )
        )

        response_text = chatbot_response.text.strip()
        
        # Add chatbot response to history
        conversation_history.append(f"Bot: {response_text}")

        # Display formatted response
        print(f"\nBot: {response_text}\n")
        print("-" * 60)
        
    except Exception as e:
        print(f"✗ Error: {str(e)}\n")

    user_input = input("You: ").strip()

# Display exit message
print("\n" + "=" * 60)
print(f"Chat ended. Total messages: {message_count}".center(60))
print("=" * 60 + "\n")
