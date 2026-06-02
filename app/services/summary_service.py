from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from app.llm.mistral_client import (
    get_llm
)


class SummaryService:

    def __init__(self):

        self.llm = get_llm()

    def summarize(
            self,
            transcript: str
    ):

        prompt = (
            ChatPromptTemplate
            .from_messages(
                [
                    (
                        "system",
                        """
Create a concise
video summary.
"""
                    ),
                    (
                        "human",
                        "{text}"
                    ),
                ]
            )
        )

        chain = (
            prompt
            | self.llm
            | StrOutputParser()
        )

        return chain.invoke(
            {"text": transcript}
        )

    def generate_title(
            self,
            transcript: str
    ):

        prompt = (
            ChatPromptTemplate
            .from_messages(
                [
                    (
                        "system",
                        """
Generate a short
professional title.

Maximum 8 words.
"""
                    ),
                    (
                        "human",
                        "{text}"
                    ),
                ]
            )
        )

        chain = (
            prompt
            | self.llm
            | StrOutputParser()
        )

        return chain.invoke(
            {
                "text":
                    transcript[:2000]
            }
        )

    def extract_action_items(
            self,
            transcript: str
    ):

        prompt = (
            ChatPromptTemplate
            .from_messages(
                [
                    (
                        "system",
                        """
Extract all
action items.
"""
                    ),
                    (
                        "human",
                        "{text}"
                    ),
                ]
            )
        )

        chain = (
            prompt
            | self.llm
            | StrOutputParser()
        )

        return chain.invoke(
            {"text": transcript}
        )