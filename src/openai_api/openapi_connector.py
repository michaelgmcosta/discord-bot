import openai
import os
from dotenv import load_dotenv
from typing import Dict, List, Any

load_dotenv()

openai.api_key = os.environ.get("CHAT_GTP_API_KEY")


def get_chat_gpt_response(question: str) -> str | None:
    response_from_chat_gpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}]
    )

    if response_from_chat_gpt:
        choices: List[Dict[str, Any]] = response_from_chat_gpt.get("choices", None)
        if choices and len(choices) > 0:
            message = choices[0].get("message", None)
            text: str = message.get("content", None)
            return text
    return None
