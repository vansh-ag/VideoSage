import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

def get_llm(
    temperature: float = 0.3
):
    return ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=os.getenv(
            "MISTRAL_API_KEY"
        ),
        temperature=temperature,
    )