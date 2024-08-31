from src.data_preparation import create_embeddings
from src.utils.file_io import load_data
import argparse
import numpy as np
import os 

from src.CONSTANT import DEFAULT_JSON_PATH

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_path", type=str, default=DEFAULT_JSON_PATH)
    args = parser.parse_args()

    parent_path = directory_path = os.path.dirname(args.json_path)
    if not os.path.exists(parent_path):
        os.makedirs(parent_path)
    else:
        print("data 폴더가 이미 존재함.")
    
    data = load_data(args.json_path)
    annotations = [item['annotation'] for item in data]

    embeddings, model = create_embeddings(annotations)
    np.save('embeddings.npy', embeddings)

