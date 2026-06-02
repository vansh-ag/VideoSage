import os
from pydub import AudioSegment

WAV_DIR = "data/audio/wav"
CHUNK_DIR = "data/audio/chunks"

os.makedirs(WAV_DIR, exist_ok=True)
os.makedirs(CHUNK_DIR, exist_ok=True)


def convert_to_wav(input_path: str) -> str:
    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"File not found: {input_path}"
        )

    filename = os.path.splitext(
        os.path.basename(input_path)
    )[0]

    output_path = os.path.join(
        WAV_DIR,
        f"{filename}.wav"
    )

    audio = AudioSegment.from_file(
        input_path
    )

    audio = (
        audio
        .set_channels(1)
        .set_frame_rate(16000)
    )

    audio.export(
        output_path,
        format="wav"
    )

    return output_path


def chunk_audio(
    wav_path: str,
    chunk_minutes: int = 10
) -> list[str]:

    if not os.path.exists(wav_path):
        raise FileNotFoundError(
            f"File not found: {wav_path}"
        )

    audio = AudioSegment.from_wav(
        wav_path
    )

    chunk_ms = (
        chunk_minutes
        * 60
        * 1000
    )

    chunks = []

    base_name = os.path.splitext(
        os.path.basename(wav_path)
    )[0]

    for i, start in enumerate(
        range(
            0,
            len(audio),
            chunk_ms
        )
    ):
        chunk = audio[
            start:
            start + chunk_ms
        ]

        chunk_path = os.path.join(
            CHUNK_DIR,
            f"{base_name}_chunk_{i}.wav"
        )

        chunk.export(
            chunk_path,
            format="wav"
        )

        chunks.append(
            chunk_path
        )

    return chunks


def delete_chunks(
    chunk_paths: list[str]
) -> None:

    for path in chunk_paths:
        if os.path.exists(path):
            os.remove(path)