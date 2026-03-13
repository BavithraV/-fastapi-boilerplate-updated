import json


def parse_llm_output(text: str):

    try:

        data = json.loads(text)

        return data

    except Exception:

        raise ValueError("Invalid LLM response format")