# 🎥 VideoSage - AI-Powered Video RAG Assistant

VideoSage is an AI-powered Retrieval-Augmented Generation (RAG) application that transforms videos, audio recordings, and YouTube content into an interactive knowledge base. Instead of manually watching hours of content to find specific information, users can simply ask questions in natural language and receive accurate, context-aware answers grounded in the original media.

The system automatically extracts audio from multimedia sources, generates transcripts using OpenAI Whisper, converts text into vector embeddings, stores them in ChromaDB, and uses Mistral AI to generate intelligent responses based on the most relevant retrieved context.

## 🚀 Problem Statement

Modern digital content such as lectures, webinars, podcasts, interviews, meetings, and tutorials often contains valuable information hidden within hours of recordings. Traditional search methods require users to manually navigate timelines, rewatch content, or rely on incomplete notes.

Common challenges include:

* Finding specific information within long videos.
* Extracting insights from large volumes of multimedia content.
* Understanding content without watching entire recordings.
* Searching videos beyond simple keyword matching.
* Retrieving contextual answers from spoken conversations.

VideoSage solves these challenges by enabling conversational interaction with multimedia content through Retrieval-Augmented Generation (RAG).

## 💡 Solution

VideoSage converts unstructured video and audio data into a searchable semantic knowledge base. Users can upload media files or provide YouTube URLs and instantly query the content using natural language.

The platform:

* Transcribes spoken content automatically.
* Creates semantic vector representations of transcripts.
* Retrieves the most relevant content for a user query.
* Generates context-aware responses using an LLM.
* Provides source attribution and timestamps for transparency.

## ✨ Features

* Upload MP4, MP3, WAV, MOV, and MKV files
* Process YouTube videos via URL
* Automatic audio extraction and conversion
* Whisper-powered speech-to-text transcription
* Optional transcript translation
* Semantic search using vector embeddings
* ChromaDB vector database integration
* Retrieval-Augmented Generation (RAG)
* Mistral-powered question answering
* Source attribution with timestamps
* Interactive Streamlit interface
* Support for long-form multimedia content

## ⚙️ How It Works

1. **Content Ingestion**

   * Accepts YouTube URLs, video files, and audio recordings.

2. **Audio Processing**

   * Extracts and standardizes audio using FFmpeg and Pydub.

3. **Speech Recognition**

   * Generates transcripts using OpenAI Whisper.

4. **Text Chunking**

   * Splits transcripts into semantically meaningful chunks.

5. **Embedding Generation**

   * Creates vector embeddings using Sentence Transformers.

6. **Vector Storage**

   * Stores embeddings in ChromaDB for efficient retrieval.

7. **Semantic Retrieval**

   * Retrieves the most relevant transcript segments for a query.

8. **Answer Generation**

   * Mistral AI generates grounded responses using retrieved context.

## 🏗️ Architecture

Input Source (YouTube / Video / Audio)

↓
Audio Extraction & Processing

↓
Whisper Transcription

↓
Transcript Chunking

↓
Embedding Generation

↓
ChromaDB Vector Storage

↓
Semantic Retrieval

↓
Mistral AI

↓
Context-Aware Answer Generation

## 🛠️ Tech Stack

### AI & LLM

* Whisper
* Mistral AI
* LangChain

### RAG Pipeline

* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings

### Backend & Processing

* Python
* yt-dlp
* FFmpeg
* Pydub

### Frontend

* Streamlit

## 🎯 Real-World Use Cases

* Educational lecture assistants
* Podcast knowledge retrieval
* Meeting and interview analysis
* Webinar summarization
* Research content exploration
* Corporate training search systems
* Content creator productivity tools
* Video-based customer support systems

## 📂 Project Structure

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

## 🔮 Future Improvements

* FastAPI Backend
* Multi-Video Knowledge Base
* Persistent Chat History
* Speaker Diarization
* Timestamp Navigation
* Hybrid Search (Keyword + Semantic Search)
* User Authentication & Workspaces
* Multi-Language Support
* Cloud Deployment
* Team Collaboration Features

## Clone Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/<your-username>/VideoSage.git
cd VideoSage
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install FFmpeg

VideoSage requires FFmpeg for audio extraction and processing.

Verify installation:

```bash
ffmpeg -version
ffprobe -version
```

## Configure Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
WHISPER_MODEL=small
```

## Run VideoSage

```bash
streamlit run streamlit_app.py
```

After launching, open the Streamlit URL displayed in the terminal (typically `http://localhost:8501`).

## Quick Test

1. Upload a video/audio file or provide a YouTube URL.
2. Click **Process Content**.
3. Wait for transcription and indexing.
4. Ask questions about the content.
5. Receive timestamp-aware answers generated using RAG and Mistral AI.

```
```

## 👨‍💻 Author

**Vansh Agarwal**

AI/ML Engineer | GenAI Developer | Software Engineer
