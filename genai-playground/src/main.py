from config.prompt_config import GenerationConfig
from models.request import GenerationRequest
from services.generator_service import GeneratorService

config = GenerationConfig()
service = GeneratorService()

# Display welcome banner
print("=" * 60)
print("🤖  CHATBOT  🤖".center(60))
print("=" * 60)
print("Type 'exit' to exit the conversation  •  Press Enter to send\n")

provider = input("🔌 Select provider (ollama | gemini | openai): ").strip().lower()
if provider:
    print(f"Selected provider: {provider} ✅\n")

request = GenerationRequest(prompt="", provider=provider, config=config)

# Get initial user input
user_input = input("🧑 You: ").strip()

while user_input.lower() != "exit":
    request.prompt = user_input
    response = service.generate(request)

    if request.config.stream:
        print("✨ Bot: ", end="", flush=True)
        for chunk in response:
            print(chunk, end="", flush=True)
        print()
    else:
        print(f"✨ Bot: {response}")

    user_input = input("\n🧑 You: ").strip()

print("\n" + "=" * 60)
print("👋 Chat ended. Thanks for chatting! ✨")
print("=" * 60 + "\n")