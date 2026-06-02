import os

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.embeddings.embedding_model import (
    get_embedding_model
)

CHROMA_DIR = "chroma_db"

os.makedirs(
    CHROMA_DIR,
    exist_ok=True
)


def get_collection_name(
    source_name: str
) -> str:

    return (
        source_name
        .replace(" ", "_")
        .replace(".", "_")
        .lower()
    )


def create_documents(
    transcript_data: dict,
    source_name: str
):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = []

    for segment in transcript_data[
        "segments"
    ]:

        chunks = splitter.split_text(
            segment["text"]
        )

        for chunk in chunks:

            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "source": source_name,
                        "start": segment["start"],
                        "end": segment["end"]
                    }
                )
            )

    return documents


def build_vector_store(
    transcript_data: dict,
    source_name: str
):

    print(
        "Building Vector Store..."
    )

    collection_name = (
        get_collection_name(
            source_name
        )
    )

    documents = create_documents(
        transcript_data,
        source_name
    )

    embeddings = (
        get_embedding_model()
    )

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory=CHROMA_DIR
    )

    print(
        f"Stored {len(documents)} chunks"
    )

    return vector_store


def load_vector_store(
    source_name: str
):

    collection_name = (
        get_collection_name(
            source_name
        )
    )

    embeddings = (
        get_embedding_model()
    )

    return Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR
    )


def get_retriever(
    vector_store,
    k: int = 4
):

    return (
        vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": k
            }
        )
    )


def similarity_search(
    query: str,
    source_name: str,
    k: int = 4
):

    store = load_vector_store(
        source_name
    )

    return store.similarity_search(
        query,
        k=k
    )