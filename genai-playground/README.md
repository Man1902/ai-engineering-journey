# genai-playground

Lightweight playground for experimenting with generation providers (Ollama, Gemini, OpenAI).

## Overview

This folder contains a minimal chatbot-style generator example that demonstrates provider selection, streaming and non-streaming outputs, and simple prompt configuration.

Key file:

- `src/main.py` — interactive CLI that prompts for a provider and chat input. The output includes emojis and a streaming-friendly display.

## Requirements

- Python 3.10+
- Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Quickstart

Run the interactive chat from the repository root:

```bash
python genai-playground/src/main.py
```

Or from inside the `genai-playground` folder:

```bash
python src/main.py
```

Follow the prompts:

- Select a provider when asked (e.g. `ollama`, `gemini`, or `openai`).
- Type messages and press Enter to send. Type `exit` to quit.

The CLI now shows emojis and improved streaming formatting (flushed chunks and a final newline) for a better user experience.

## Configuration

Prompt and generation settings are in `src/config/prompt_config.py`.

## Notes

- If you enable streaming in the configuration, the bot prints chunks as they arrive and flushes the output for responsiveness.
- If you integrate a new provider, add a provider implementation under `src/providers` and register it in the provider factory.

## Virtual environment (recommended)

Create and activate a virtual environment to isolate dependencies:

On Windows (PowerShell):

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

After activation, run the CLI as shown in the Quickstart section.
