from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Load Data
def load_pdf(data):
    loader = DirectoryLoader(data,
                            glob = "*.pdf",
                            loader_cls = PyPDFLoader)
    documents = loader.load()
    return documents

# Text Splitting into chunks
def text_split(data_pdf):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap= 50)
    text_chunks = text_splitter.split_documents(data_pdf)
    return text_chunks


def HF_Embeddings():
    embeddings = HuggingFaceEmbeddings(model_name= 'sentence-transformers/all-MiniLM-L6-v2')
    return embeddings




