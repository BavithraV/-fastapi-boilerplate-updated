from openai import OpenAI
from app.config.settings import settings
from app.utils.constants import DEFAULT_TEMPERATURE, MAX_TOKENS

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def call_llm(prompt: str) -> str:

    response = client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        temperature=DEFAULT_TEMPERATURE,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": "You are an AI evaluator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content