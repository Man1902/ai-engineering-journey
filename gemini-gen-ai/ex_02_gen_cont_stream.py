from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image

GEMINI_MODEL = "gemini-2.5-flash"

# load GEMINI_API_KEY enviroment varialbe
load_dotenv()

client = genai.Client()

image = Image.open("images/cat.jpg")

is_running = True
while is_running:
    prompt = input("Enter your prompt (Enter q to quit): ")

    if prompt.lower() == "q":
        is_running = False
    else:
        response = client.models.generate_content_stream(
            model=GEMINI_MODEL,
            contents=[image, prompt],
            config=types.GenerateContentConfig(
                system_instruction="response should be within 200 words",
                temperature=0.1,
            )
        )

        print("\n", 30 * "-", "Response", 30 * "-")
        for chunk in response:
            print(chunk.text, end="", flush=True) 
        print(68 * "-", "\n")
