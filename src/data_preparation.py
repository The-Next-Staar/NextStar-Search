import json
import numpy as np
from sentence_transformers import SentenceTransformer

def load_data(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)

def create_embeddings(annotations):
    model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
    embeddings = model.encode(annotations)
    return embeddings, model

if __name__ == "__main__":
    data = load_data('data/raw_annotation.json')
    annotations = [item['annotation'] for item in data]

    embeddings, model = create_embeddings(annotations)
    np.save('embeddings.npy', embeddings)
