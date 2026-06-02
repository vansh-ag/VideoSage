from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from langchain_core.runnables import (
    RunnablePassthrough,
    RunnableLambda
)

from app.llm.mistral_client import (
    get_llm
)

from app.rag.retriever import (
    get_retriever
)


def format_docs(docs):

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


def build_rag_chain(
    source_name: str
):

    retriever = get_retriever(
        source_name
    )

    llm = get_llm()

    prompt = (
        ChatPromptTemplate
        .from_messages(
            [
                (
                    "system",
                    """
You are an expert Video Assistant.

Answer ONLY from the provided context.

If the answer is not found, say:

"I could not find this information in the video."

If relevant information is found, provide a concise answer.

Context:
{context}
"""
                ),
                (
                    "human",
                    "{question}"
                ),
            ]
        )
    )

    rag_chain = (
        {
            "context":
                retriever
                | RunnableLambda(
                    format_docs
                ),

            "question":
                RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain