import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
DEFAULT_MODEL = os.getenv(
    "LIFEGRAPH_MODEL",
    "openai/gpt-4.1-mini",
)
