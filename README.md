# 🎥 VideoSage - Video RAG Assistant

VideoSage is an AI-powered Video RAG (Retrieval-Augmented Generation) application that enables users to chat with videos, audio recordings, and YouTube content.

The system extracts audio, generates transcripts using Whisper, creates embeddings, stores them in ChromaDB, and answers user questions using Mistral AI.

## Features

* Upload MP4, MP3, WAV, MOV, and MKV files
* Process YouTube videos using URL input
* Automatic audio extraction and conversion
* Whisper-based speech-to-text transcription
* Optional transcript translation
* ChromaDB vector database
* Semantic search with sentence-transformers embeddings
* Mistral-powered question answering
* Source attribution with timestamps
* Streamlit user interface

## Architecture

Input Source

→ Audio Extraction

→ Whisper Transcription

→ Text Chunking

→ Embedding Generation

→ ChromaDB Storage

→ Retrieval

→ Mistral LLM

→ Answer Generation

## Tech Stack

### AI & LLM

* Whisper
* Mistral AI
* LangChain

### RAG

* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings

### Backend

* Python
* yt-dlp
* FFmpeg
* Pydub

### Frontend

* Streamlit

## Project Structure

video-rag/

├── app/

│ ├── embeddings/

│ ├── ingestion/

│ ├── llm/

│ ├── rag/

│ ├── services/

│ ├── transcription/

│ ├── translation/

│ └── vectordb/

├── chroma_db/

├── data/

├── streamlit_app.py

├── requirements.txt

├── .env

└── README.md

## Installation

Clone the repository

```bash
git clone <repository-url>
cd VideoSage
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install FFmpeg

Verify installation

```bash
ffmpeg -version
ffprobe -version
```

## Environment Variables

Create a .env file

```env
MISTRAL_API_KEY=your_mistral_api_key
WHISPER_MODEL=small
```

## Run Application

```bash
streamlit run streamlit_app.py
```

## Usage

1. Upload a video/audio file or provide a YouTube URL.
2. Process the content.
3. Wait for transcription and indexing.
4. Ask questions about the content.
5. View answers with timestamps.

## Current Phase

Phase 1 Features

* Video & Audio Upload
* YouTube URL Processing
* Whisper Transcription
* ChromaDB Vector Store
* Semantic Search
* Mistral QA
* Streamlit Interface

## Future Improvements

* FastAPI Backend
* Multi-video Knowledge Base
* Chat History
* Speaker Diarization
* Video Timestamp Navigation
* Hybrid Search
* User Authentication

## Author

Vansh Agarwal
