# AI-Calorie-Assistant-RAG-LLM-Docker-
An AI-powered calorie assistant that answers food-related queries using Retrieval-Augmented Generation (RAG) with OpenAI GPT-3.5 and Pinecone.



## Features

* Natural language calorie queries
* PDF-based knowledge ingestion
* RAG pipeline (retrieval + generation)
* FastAPI backend + Gradio UI
* Dockerized multi-service setup
* AWS deployment ready

---

## How It Works

1. PDF → Text extraction
2. Text → Embeddings
3. Stored in Pinecone
4. Query → Relevant context retrieved
5. GPT-3.5 generates answer

---

## Architecture

```text
User → Gradio UI → FastAPI → Pinecone → OpenAI GPT → Response
```

---

## Project Structure

```text
app/
├── config.py       # Config & environment variables
├── ingest.py       # PDF ingestion & embeddings
├── rag.py          # RAG pipeline
├── main.py         # FastAPI backend
└── gradio_ui.py    # Gradio UI

Data/the-calorie-chart-of-indian-food.pdf
Dockerfile.api
Dockerfile.ui
docker-compose.yml
requirements.txt
.dockerignore
.env
```

---

## Environment Variables

```env
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=your_env
```

---

## Run Locally

```bash
docker-compose up --build
```

---

## Access

* UI → http://localhost:7860
* API → http://localhost:8000

---

## Docker Optimization

This project includes best practices for efficient Docker builds:

* ✅ `requirements.txt` installed first for caching layers
* ✅ `.dockerignore` reduces build context size
* ✅ Separate Dockerfiles for API and UI
* ✅ Faster rebuilds with minimal layer invalidation

---

## AWS Deployment

### 1. Launch EC2

* Enable public IP
* Open ports: 22, 8000, 7860

---

### 2. Install Docker

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
```

---

### 3. Clone Repo

```bash
git clone https://github.com/um-nath/AI-Calorie-Assistant-RAG-LLM-Docker-.git
cd ai-calorie-assistant
```

---

### 4. Run Application

```bash
docker-compose up -d
```

---

### 5. Access

```text
http://YOUR_PUBLIC_IP:7860
```

---

## 🧠 Learnings

* RAG pipeline design
* Vector database usage (Pinecone)
* Docker multi-container architecture
* AWS deployment & networking
* Build optimization techniques

---

## Contact

Feel free to connect or contribute!

---

## Author 
 Ujjwal Manikya Nath
