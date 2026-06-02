import streamlit as st

from app.ingestion.youtube_loader import (
    download_youtube_audio
)

from app.ingestion.file_loader import (
    save_uploaded_file
)

from app.ingestion.audio_extractor import (
    convert_to_wav,
    chunk_audio,
    delete_chunks
)

from app.transcription.whisper_transcriber import (
    transcribe_audio
)

from app.translation.translator import (
    translate_transcript
)

from app.vectordb.chroma_store import (
    build_vector_store
)

from app.services.summary_service import (
    SummaryService
)

from app.services.query_service import (
    QueryService
)

from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]

    query = parse_qs(
        urlparse(url).query
    )

    return query.get(
        "v",
        ["youtube_video"]
    )[0]


st.set_page_config(
    page_title="Video RAG Assistant",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 Video RAG Assistant")
st.caption(
    "Upload videos, audio files, or YouTube links and chat with them."
)

if "processed" not in st.session_state:
    st.session_state.processed = False

if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "source_name" not in st.session_state:
    st.session_state.source_name = None

st.sidebar.header("Upload Source")

source_type = st.sidebar.radio(
    "Choose Input",
    [
        "YouTube URL",
        "File Upload"
    ]
)

translate_enabled = st.sidebar.checkbox(
    "Translate to English",
    value=False
)

youtube_url = None
uploaded_file = None

if source_type == "YouTube URL":

    youtube_url = st.sidebar.text_input(
        "Enter YouTube URL"
    )

else:

    uploaded_file = st.sidebar.file_uploader(
        "Upload File",
        type=[
            "mp4",
            "mp3",
            "wav",
            "mov",
            "mkv"
        ]
    )

if st.sidebar.button("Process"):

    try:

        with st.spinner(
            "Processing video..."
        ):

            if source_type == "YouTube URL":

                if not youtube_url:
                    st.warning(
                        "Please enter a YouTube URL."
                    )
                    st.stop()

                wav_path = (
                    download_youtube_audio(
                        youtube_url
                    )
                )

                source_name = get_video_id(
                    youtube_url
                )

            else:

                if uploaded_file is None:
                    st.warning(
                        "Please upload a file."
                    )
                    st.stop()

                file_path = (
                    save_uploaded_file(
                        uploaded_file
                    )
                )

                wav_path = (
                    convert_to_wav(
                        file_path
                    )
                )

                source_name = (
                    uploaded_file.name
                )

            chunks = chunk_audio(
                wav_path
            )

            transcript_data = (
                transcribe_audio(
                    chunks,
                    "transcript"
                )
            )

            delete_chunks(
                chunks
            )

            if translate_enabled:

                transcript_data = (
                    translate_transcript(
                        transcript_data
                    )
                )

            build_vector_store(
                transcript_data,
                source_name
            )

            summary_service = (
                SummaryService()
            )

            summary = (
                summary_service.summarize(
                    transcript_data[
                        "full_text"
                    ]
                )
            )

            st.session_state.summary = (
                summary
            )

            st.session_state.transcript = (
                transcript_data
            )

            st.session_state.source_name = (
                source_name
            )

            st.session_state.processed = True

            st.success(
                "Video processed successfully!"
            )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

if st.session_state.processed:

    tab1, tab2, tab3 = st.tabs(
        [
            "Summary",
            "Transcript",
            "Chat"
        ]
    )

    with tab1:

        st.subheader(
            "Video Summary"
        )

        st.write(
            st.session_state.summary
        )

    with tab2:

        st.subheader(
            "Transcript"
        )

        st.text_area(
            "",
            value=st.session_state.transcript[
                "full_text"
            ],
            height=400
        )

    with tab3:

        st.subheader(
            "Ask Questions"
        )

        question = st.text_input(
            "Enter your question"
        )

        if st.button("Ask"):

            query_service = (
                QueryService(
                    st.session_state.source_name
                )
            )

            result = (
                query_service.answer_question(
                    question
                )
            )

            st.markdown(
                "### Answer"
            )

            st.write(
                result["answer"]
            )

            st.markdown(
                "### Sources"
            )

            for source in result[
                "sources"
            ]:

                st.info(
                    f"""
Source: {source['source']}

Time: {source['start']:.2f}s - {source['end']:.2f}s
"""
                )