from app.rag.rag_pipeline import build_rag_chain
from app.rag.retriever import retrieve_context


class QueryService:

    def __init__(
        self,
        source_name: str
    ):
        self.source_name = source_name

        self.rag_chain = build_rag_chain(
            source_name
        )

    def answer_question(
        self,
        question: str
    ):

        docs = retrieve_context(
            query=question,
            source_name=self.source_name
        )

        answer = self.rag_chain.invoke(
            question
        )

        sources = []

        for doc in docs:
            sources.append(
                {
                    "source": doc.metadata.get(
                        "source",
                        "Unknown"
                    ),
                    "start": doc.metadata.get(
                        "start",
                        0
                    ),
                    "end": doc.metadata.get(
                        "end",
                        0
                    )
                }
            )

        return {
            "answer": answer,
            "sources": sources
        }