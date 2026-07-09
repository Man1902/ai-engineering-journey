from google import genai
from google.genai import types
from dotenv import load_dotenv
from datetime import datetime

GEMINI_MODEL = "gemini-2.5-flash"

# Load GEMINI_API_KEY environment variable
load_dotenv()

client = genai.Client()

# Create a chat session (Note: no need to maintain conversation history manually, as the chat session handles it)
chat =client.chats.create(model=GEMINI_MODEL)

# Display welcome banner
print("\n" + "=" * 60)
print("✓ GEMINI CHATBOT".center(60))
print("=" * 60)
print("Type 'endchat' to exit the conversation.\n")

message_count = 0

# Get initial user input
user_input = input("You: ").strip()

while user_input.lower() != "endchat":
    if not user_input:
        print("⚠ Please enter a message.\n")
        user_input = input("You: ").strip()
        continue

    message_count += 1
    
    try:
        # Get chatbot response
        chatbot_response = chat.send_message( 
           message=user_input,
           config=types.GenerateContentConfig(
                system_instruction="Answer in 1 line, within 50 words.",
                temperature=0.1,
            )
        )
        response_text = chatbot_response.text.strip()
        
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

# optionally, display the entire chat history
# print("Chat History:")
# for message in chat.get_history():
#     role = "You" if message.role.lower() == "user" else "Bot"
#     print(f"{role}: {message.parts[0].text.strip()}")
