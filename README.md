# SuperTeam AI Assistant

A FastAPI and LangChain-based AI assistant with local LLM integration through Ollama, featuring a Telegram bot interface and document processing capabilities. Created by [@eniiku]("https://github.com/eniiku"), and [@eskayML]("https://github.com/eskayML")

## Architecture

```
├── api/
│   ├── app.py              # FastAPI application
│   └── templates/          # HTML templates
├── superteam_ai/
│   ├── bot/               # Telegram bot implementation
│   │   ├── __init__.py
│   │   └── telegram_bot.py
│   ├── config/           # Configuration management
│   ├── document_processor/ # Document processing utilities
│   ├── llm/              # Local LLM integration
│   │   ├── __init__.py
│   │   └── local-llm.py
│   └── utils/            # Utility functions
├── tests/                # Test suite
└── requirements.txt      # Project dependencies
```

## Core Components

### Local LLM Integration

- Uses Ollama for local model inference
- Implements RAG (Retrieval Augmented Generation)
- ChromaDB for vector storage
- Document processing with LangChain

### FastAPI Backend

- File upload endpoints
- Document processing
- HTML interface

### Telegram Bot

- Interactive chat interface
- RAG-based responses
- Conversation history tracking

## Prerequisites

- Python 3.8+
- Ollama installed locally with required models:
  - deepseek-r1:1.5b
  - nomic-embed-text

## Setup

1. Clone the repository:

```bash
git clone https://github.com/eniiku/SuperteamAIAssistant.git
cd SuperteamAIAssistant
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
```

## Usage

### Starting the API Server

```bash
uvicorn api.app:app --reload
```

Access the web interface at `http://localhost:8000`

### Running the Telegram Bot

```bash
python -m superteam_ai.bot.telegram_bot
```

## API Endpoints

### File Upload

- `POST /upload/`: Upload single document
- `POST /upload-multiple/`: Upload multiple documents

Supported file extensions: `.txt`, `.pdf`, `.doc`, `.docx`

## Core Features

### Document Processing

- Supports PDF, DOCX, and JSON files
- Automatic document chunking
- Efficient vector embeddings

### Local LLM Integration

- Uses Ollama for local model inference
- Supports multiple model configurations
- Efficient document retrieval

### Telegram Bot

- Interactive chat interface
- Document processing capabilities
- Configurable response generation

## Authors

- Initial work - [eniiku & eskayML]

## License

MIT
