import os
import yt_dlp

RAW_AUDIO_DIR = "data/raw/audio"
os.makedirs(RAW_AUDIO_DIR, exist_ok=True)


def download_youtube_audio(url: str) -> str:
    """
    Download audio from YouTube and convert to WAV.
    Returns path to downloaded WAV file.
    """

    output_path = os.path.join(
        RAW_AUDIO_DIR,
        "%(title)s.%(ext)s"
    )

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            url,
            download=True
        )

        filename = (
            ydl.prepare_filename(info)
            .replace(".webm", ".wav")
            .replace(".m4a", ".wav")
        )

    return filename