from src.CONSTANT import model_name
import json
import numpy as np
from sentence_transformers import SentenceTransformer

def create_embeddings(annotations):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(annotations)
    return embeddings, model