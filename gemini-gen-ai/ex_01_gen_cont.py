from google import genai
from dotenv import load_dotenv

GEMINI_MODEL = "gemini-2.5-flash"

# load GEMINI_API_KEY enviroment varialbe
load_dotenv()

client = genai.Client()

is_running = True
while is_running:
    prompt = input("Enter your prompt (Enter q to quit): ")

    if prompt.lower() == "q":
        is_running = False
    else:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt 
        )

        print("\n", 30 * "-", "Response", 30 * "-")
        print(response.text)
        print(68 * "-", "\n")
