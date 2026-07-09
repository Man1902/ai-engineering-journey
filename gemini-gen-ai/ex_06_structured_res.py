from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel
import enum

GEMINI_MODEL = "gemini-2.5-flash"

class Grade(enum.Enum):
    A_PLUS = "a+"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    F = "f"

class Recipe(BaseModel):
    name: str
    ingredients: list[str]
    rating: Grade

# Load GEMINI_API_KEY environment variable
load_dotenv()

client = genai.Client()

prompt = "List a two popular chocolate recipes, and include the amounts of ingredients needed for each recipe."

response = client.models.generate_content(
    model=GEMINI_MODEL,
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe]
    }
)

print(response.text)