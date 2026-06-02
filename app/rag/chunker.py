from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def split_segments(
        transcript_data: dict,
        chunk_size: int = 500,
        chunk_overlap: int = 50
):
    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    )

    chunks = []

    for segment in transcript_data[
        "segments"
    ]:

        texts = splitter.split_text(
            segment["text"]
        )

        for text in texts:

            chunks.append(
                {
                    "text": text,
                    "start": segment["start"],
                    "end": segment["end"]
                }
            )

    return chunks