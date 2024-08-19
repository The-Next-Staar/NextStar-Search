import faiss
import numpy as np
import shutil
import os

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_and_save_results(query, model, index, data, top_k=3):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=top_k)

    if not os.path.exists('result'):
        os.makedirs('result')
    
    results = []
    for idx in I[0]:
        item = data[idx]
        image_path = item['image']
        dest_path = os.path.join('result', os.path.basename(image_path))
        
        shutil.copy(image_path, dest_path)
        
        results.append({
            'id': item['id'],
            'category': item['category'],
            'image': dest_path,
            'annotation': item['annotation'],
            'name': item['name']
        })
    
    return results

if __name__ == "__main__":
    data = np.load('embeddings.npy')
    index = create_faiss_index(data)
