from langchain_huggingface import HuggingFaceEmbeddings
import torch

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

def get_embedding_model():

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={
            "device": DEVICE
        }
    )