from google import genai
from google.genai import types
from dotenv import load_dotenv
import httpx, pathlib

GEMINI_MODEL = "gemini-2.5-flash"

# Load GEMINI_API_KEY environment variable
load_dotenv()

client = genai.Client()


# doc_url = ""
# doc_data = httpx.get(doc_url).content

file_path = pathlib.Path("pdfs/sample1.pdf")
doc_data = file_path.read_bytes()

pdf = types.Part.from_bytes(
    data=doc_data,
    mime_type="application/pdf"
)

prompt = "Summarize the document"

response = client.models.generate_content(
    model=GEMINI_MODEL,
    contents=[pdf, prompt],
    config=types.GenerateContentConfig(
        system_instruction="Answer within 100 words.",
        temperature=0.1,
    )
)

print("\n", 30 * "-", "Response", 30 * "-")
print(response.text)