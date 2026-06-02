import os
import shutil

UPLOAD_DIR = "data/raw/uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


def save_uploaded_file(
        uploaded_file,
):
    """
    Save uploaded file locally.

    Streamlit:
    uploaded_file = st.file_uploader(...)
    """

    file_path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def validate_file(
        file_path: str
):
    """
    Check supported formats.
    """

    allowed_extensions = [
        ".mp4",
        ".mp3",
        ".wav",
        ".mkv",
        ".mpeg"
    ]

    ext = os.path.splitext(file_path)[1]

    if ext.lower() not in allowed_extensions:
        raise ValueError(
            f"Unsupported file format: {ext}"
        )

    return True