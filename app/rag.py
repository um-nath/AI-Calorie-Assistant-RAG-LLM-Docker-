import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore



#### ENV VALIDATION
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Missing OPENAI_API_KEY")

if not os.getenv("PINECONE_API_KEY"):
    raise ValueError("Missing PINECONE_API_KEY")

if not os.getenv("PINECONE_INDEX"):
    raise ValueError("Missing PINECONE_INDEX")


#### LOAD RETRIEVER
def get_retriever():

    embeddings = OpenAIEmbeddings()

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index_name = os.getenv("PINECONE_INDEX")

    vectorstore = PineconeVectorStore(
        index_name=index_name,
        embedding=embeddings,
        namespace="calorie-content" 
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    return retriever


#### FORMAT DOCUMENTS
def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


##### LOAD QA CHAIN
def load_qa_chain():

    retriever = get_retriever()

    
    # Promt
    prompt_template = """
You are a helpful AI assistant.

Answer the question using ONLY the provided context.
If the answer is not in the context, say:
"I don't have enough information from the document."

Context:
{context}

Question:
{question}

Answer clearly and concisely:
"""
    

    prompt = PromptTemplate(
        template= prompt_template,
        input_variables=["context", "question"]
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    chain = (
        {
            "context": retriever | format_docs,
            "question": lambda x: x
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain