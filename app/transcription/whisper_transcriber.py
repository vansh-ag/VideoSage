import os
import json
import whisper

WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL",
    "small"
)

TRANSCRIPT_DIR = "data/transcripts"

os.makedirs(
    TRANSCRIPT_DIR,
    exist_ok=True
)

_model = None


def load_model():

    global _model

    if _model is None:

        print(
            f"Loading Whisper model: "
            f"{WHISPER_MODEL}"
        )

        _model = whisper.load_model(
            WHISPER_MODEL
        )

        print(
            "Whisper model loaded."
        )

    return _model


def transcribe_chunk(
    chunk_path: str,
    chunk_index: int = 0
):

    model = load_model()

    result = model.transcribe(
        chunk_path,
        task="transcribe"
    )

    segments = []

    for segment in result["segments"]:

        segments.append(
            {
                "chunk": chunk_index,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"].strip()
            }
        )

    return {
        "text": result["text"],
        "segments": segments
    }


def transcribe_audio(
    chunks: list[str],
    transcript_name: str
):

    full_text = ""

    all_segments = []

    current_offset = 0.0

    for i, chunk in enumerate(chunks):

        print(
            f"Transcribing chunk "
            f"{i + 1}/{len(chunks)}"
        )

        result = transcribe_chunk(
            chunk,
            i
        )

        full_text += (
            result["text"]
            + " "
        )

        for seg in result["segments"]:

            all_segments.append(
                {
                    "chunk": seg["chunk"],
                    "start": round(
                        seg["start"]
                        + current_offset,
                        2
                    ),
                    "end": round(
                        seg["end"]
                        + current_offset,
                        2
                    ),
                    "text": seg["text"]
                }
            )

        if result["segments"]:

            chunk_duration = max(
                segment["end"]
                for segment
                in result["segments"]
            )

            current_offset += (
                chunk_duration
            )

    transcript_data = {
        "full_text": full_text.strip(),
        "segments": all_segments
    }

    save_transcript(
        transcript_name,
        transcript_data
    )

    print(
        "Transcription complete."
    )

    return transcript_data


def save_transcript(
    name: str,
    transcript_data: dict
):

    output_path = os.path.join(
        TRANSCRIPT_DIR,
        f"{name}.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            transcript_data,
            f,
            ensure_ascii=False,
            indent=4
        )

    return output_path


def load_transcript(
    transcript_name: str
):

    path = os.path.join(
        TRANSCRIPT_DIR,
        f"{transcript_name}.json"
    )

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Transcript not found: {path}"
        )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)