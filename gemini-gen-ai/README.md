# Gemini Gen AI Examples

A small collection of Python examples showing how to use the Google Gemini API with the Google Gen AI SDK.

## Included examples

- ex_01_gen_cont.py: basic single-prompt text generation
- ex_02_gen_cont_stream.py: streaming response generation
- ex_03_chatbot.py: interactive chatbot with simple conversation flow
- ex_04_chatbot2.py: chat session example with system instructions and concise replies
- ex_05_google_search.py: grounded responses using Google Search tooling
- ex_06_structured_res.py: structured JSON output using Pydantic models
- ex_07_doc_proc.py: PDF document summarization example

## Prerequisites

- Python 3.9 or higher
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Setup

1. Create and activate a virtual environment.

   Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   macOS / Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file in this folder:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. Make sure the sample PDF exists if you want to run the document processing example:

   ```text
   pdfs/sample1.pdf
   ```

## Run the examples

```bash
python ex_01_gen_cont.py
python ex_02_gen_cont_stream.py
python ex_03_chatbot.py
python ex_04_chatbot2.py
python ex_05_google_search.py
python ex_06_structured_res.py
python ex_07_doc_proc.py
```

## Notes

- The examples use the model gemini-2.5-flash by default.
- Some scripts can be customized by changing the system instructions or temperature settings.
- Keep your API key private and avoid committing the .env file to version control.

## Dependencies

- google-genai
- python-dotenv
- pillow

See [requirements.txt](requirements.txt) for the full dependency list.
