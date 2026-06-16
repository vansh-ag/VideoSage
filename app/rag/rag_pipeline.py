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
You are VideoSage, an expert video question-answering assistant.

Your task is to answer user questions ONLY using the retrieved video transcript context.

Rules:
- Answer strictly from the provided context.
- Do not use prior knowledge.
- Do not infer facts not supported by the context.
- If multiple pieces of evidence are available, combine them into a coherent answer.
- If the context contains only partial information, provide only the supported information.
- If the answer cannot be found, respond exactly:

"I could not find this information in the video."

Response Guidelines:
- Be concise but complete.
- Use bullet points when listing multiple items.
- Preserve technical terminology from the video.
- Mention timestamps if they are present in the context.
- Never hallucinate or speculate.

Retrieved Context:
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