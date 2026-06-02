from app.vectordb.chroma_store import (
    load_vector_store
)


def get_retriever(
    source_name: str,
    k: int = 4
):

    vector_store = (
        load_vector_store(
            source_name
        )
    )

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": k
        }
    )


def retrieve_context(
    query: str,
    source_name: str,
    k: int = 4
):

    retriever = get_retriever(
        source_name,
        k
    )

    docs = retriever.invoke(
        query
    )

    return docs