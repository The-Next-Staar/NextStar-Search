import json
import numpy as np
from data_preparation import load_data
from search_system import create_faiss_index, search_and_save_results
from sentence_transformers import SentenceTransformer

if __name__ == "__main__":
    data = load_data('data/raw_annotation.json')
    embeddings = np.load('embeddings.npy')

    index = create_faiss_index(embeddings)
    
    model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
    
    query = input("검색할 내용을 입력하세요: ")
    
    results = search_and_save_results(query, model, index, data)

    for result in results:
        print(json.dumps(result, ensure_ascii=False, indent=4))
