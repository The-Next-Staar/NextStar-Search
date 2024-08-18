# 🖼️ The Next Star - Facial Image Search System

## 📋 Features

1. **Annotation Data Embedding Generation** - Converts annotation data into vectors using the Sentence Transformer model (`distiluse-base-multilingual-cased-v2` [HUGGING FACE](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2)).
2. **Search and Save Image Results** - Searches for the top 3 annotations most similar to the input query and saves the corresponding images in the `result/` directory.
3. **Similarity-Based Search** - The search is based on semantic similarity, allowing for relevant results even if the query does not exactly match any annotations.

## ⚙️ Requirements

The following Python packages are required to run this project:

- Python 3.7 or higher
- numpy
- faiss
- sentence-transformers
- scikit-learn

You can install the necessary packages with the following command:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

1. **Prepare Data and Generate Embeddings**

   Load the annotation data and generate sentence embeddings. This step will create the `embeddings.npy` file.

   ```bash
   python data_preparation.py
   ```

2. **Run the Main Program**

   The main program takes a query input from the terminal, performs the search, and outputs the results.

   ```bash
   python main.py
   ```

   Example:

   ```bash
   Enter your search query: 고양이상 눈매, 날렵한 턱선, 오똑한 코
   ```

   This command searches for the 3 most similar annotations to the query, copies the corresponding images to the `result/` directory, and prints the full details of the matched annotations to the terminal.

## 📂 Results

The search results are saved in the `result/` directory. The directory will contain the image files corresponding to the matched annotations, and the detailed information of the matched annotations will be printed in the terminal.

Example output:

```json
{
  "id": 1,
  "category": "best",
  "image": "result/image02.png",
  "annotation": "강아지상 눈매, 도회적 이미지, 차가운 이미지, 도톰한 애교살, 계란형, 뭉툭한 턱 끝, 도톰한 콧망울, 적당한 콧볼, 선명한 쌍커풀, 도톰한 아랫입술, 하얀 피부, 자기주도적성향 이미지, 여성미가 있는 얼굴, 숙녀같은 이미지",
  "name": "best_female_image02"
}
```

## ⚠️ Notes

- Be sure to run `data_preparation.py` first to generate the `embeddings.npy` file.
- Verify that the image paths and annotation data are correctly specified.
- Run `main.py` from the project’s root directory to ensure correct file paths.
