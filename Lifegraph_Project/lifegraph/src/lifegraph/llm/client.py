from openai import OpenAI

from .config import OPENROUTER_API_KEY

if not OPENROUTER_API_KEY:
    raise RuntimeError(
        "OPENROUTER_API_KEY is not set. Add it to your .env file."
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)
