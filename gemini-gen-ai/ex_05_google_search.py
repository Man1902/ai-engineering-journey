from google import genai
from google.genai import types
from dotenv import load_dotenv

GEMINI_MODEL = "gemini-2.5-flash"

# load GEMINI_API_KEY enviroment varialbe
load_dotenv()

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

response = client.models.generate_content(
    model=GEMINI_MODEL,
    contents="Who won the Euro cup 2024?",
    config=types.GenerateContentConfig(
        tools=[grounding_tool],
        system_instruction="Use the Google Search tool to find the answer if model is uncertain.",
        temperature=0.1,
    )
)

print("\n", 30 * "-", "Response", 30 * "-")
print(response)