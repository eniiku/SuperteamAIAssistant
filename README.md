# SuperTeam AI Assistant Backend

A powerful AI assistant backend system built with FastAPI and LangChain, featuring local LLM integration through Ollama and a Telegram bot interface.

## 🌟 Features

- **Local LLM Integration**: Uses Ollama for running local language models
- **Vector Store**: ChromaDB-based document storage and retrieval
- **Multiple Document Support**: Handles PDF, DOCX, and JSON files
- **API Interface**: FastAPI-based REST API
- **Telegram Bot**: Built-in Telegram bot integration
- **Document Processing**: Intelligent document chunking and embedding
- **Configurable**: Environment-based configuration system

## 🛠️ Technology Stack

- **Framework**: FastAPI
- **LLM Integration**: Ollama, LangChain
- **Vector Store**: ChromaDB
- **Document Processing**: LangChain Document Loaders
- **Bot Framework**: python-telegram-bot
- **Embeddings**: Ollama Embeddings

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Ollama installed on your system
- Telegram Bot Token (for bot functionality)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eniiku/SuperteamAIAssistant.git
   cd SuperteamAIAssistant/
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\\venv\\Scripts\\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the required LLM models with Ollama:

   ```bash
   ollama pull nomic-embed-text
   ollama pull deepseek-r1:1.5b
   ```

5. Create a .env file with your configuration:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   ```

## 🏃‍♂️ Running the Application

### Starting the API Server

```bash
uvicorn api.app:app --reload
```

The API will be available at `http://localhost:8000`

### Running the Telegram Bot

```bash
python -m superteam_ai.main
```

## 📁 Project Structure

```
backend/
├── api/
│   ├── app.py              # FastAPI application
│   └── templates/          # HTML templates
├── superteam_ai/
│   ├── bot/               # Telegram bot implementation
│   ├── config/           # Configuration management
│   ├── document_processor/ # Document processing utilities
│   ├── llm/              # Local LLM integration
│   └── utils/            # Utility functions
├── tests/                # Test suite
└── requirements.txt      # Project dependencies
```

## 🔧 Configuration

The system can be configured through environment variables:

- `TELEGRAM_TOKEN`: Your Telegram bot token
- Additional configuration can be added in `superteam_ai/config/config.py`

## 🚀 API Endpoints

- `GET /`: Web interface
- `POST /upload/`: Upload single document
- `POST /upload-multiple/`: Upload multiple documents

## 💡 Features in Detail

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

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Authors

- Initial work - [eniiku & eskayML]

---

For more information or support, please open an issue in the repository.
