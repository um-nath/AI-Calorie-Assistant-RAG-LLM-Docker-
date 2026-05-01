import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_PATH = os.path.join(BASE_DIR, "Data", "the-calorie-chart-of-indian-food.pdf")


def ingest():
    if not os.getenv("PINECONE_API_KEY"):
        raise ValueError("❌ Missing PINECONE_API_KEY")

    if not os.getenv("PINECONE_INDEX"):
        raise ValueError("❌ Missing PINECONE_INDEX")

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("❌ Missing OPENAI_API_KEY")
    
    print("📄 Loading PDF from:", PDF_PATH)

    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(f"PDF not found at {PDF_PATH}")

    # Load PDF
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    print(f"📦 Total chunks created: {len(chunks)}")

    # Embeddings
    embeddings = OpenAIEmbeddings()

    # Create vector DB (Pinecone)
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index_name = os.getenv("PINECONE_INDEX")

    vector_store = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name=index_name,
        namespace="calorie-content"
    )


    print("✅ Ingestion completed successfully!")


if __name__ == "__main__":
    ingest()