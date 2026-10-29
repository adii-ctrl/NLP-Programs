# NLP Programs

Natural Language Processing (NLP) lab programs for B.Tech CSE (Artificial Intelligence) at NIET, Greater Noida.

## Repository Structure

```text
NLP-Programs/
├── CO1/          # Programs 01-06: NLP fundamentals
├── CO2/          # Programs 07-23: NLP techniques and deep learning
├── CO3/          # Programs 24-32: Transformer and document processing
├── README.md
├── requirements.txt
└── .gitignore
```

## CO1 — NLP Fundamentals

1. Tokenization
2. Stemming and Lemmatization
3. Stopword Removal
4. Part-of-Speech (POS) Tagging
5. Parsing and Chunking
6. Named Entity Recognition (NER)

## CO2 — NLP Techniques

7. Coreference Resolution (heuristic baseline)
8. Bag-of-Words (BoW)
9. TF-IDF
10. N-Gram Models (Unigram, Bigram, Trigram)
11. Cosine Similarity
12. Word2Vec Embeddings
13. GloVe Embeddings
14. Word Mover's Distance (WMD)
15. Text Classification
16. Sentiment Analysis
17. Latent Dirichlet Allocation (LDA)
18. Latent Semantic Analysis (LSA)
19. Opinion Mining
20. Information Extraction
21. Information Retrieval
22. RNN/LSTM Sequence Classification
23. Attention Mechanism

## CO3 — Advanced NLP

24. BERT Text Classification
25. Sentence Embeddings using BERT/GPT-2 representations
26. GPT-2 Text Generation
27. Transformer-based Named Entity Recognition
28. Machine Translation using MarianMT
29. Text Summarization using BART
30. DialoGPT Chatbot
31. Document Classification and Separation
32. Hybrid Probabilistic and Finite State Machine (FSM) Document Boundary Detection

## Technologies

- Python 3.11
- NLTK and spaCy
- Gensim
- NumPy, pandas and SciPy
- Scikit-learn
- TextBlob and VADER
- TensorFlow and PyTorch
- Hugging Face Transformers and Datasets
- Git and GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/adii-ctrl/NLP-Programs.git
cd NLP-Programs
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Some spaCy programs may require the English model:

```bash
python -m spacy download en_core_web_sm
```

## Running Programs

Run programs from the repository root. For example:

```bash
python CO2/08_BOW.py
python CO2/16_Sentiment_Analysis.py
python CO3/24_BERT_Text_Classification.py
```

Use the actual filename inside the relevant folder if it differs from the example.

## Notes

- Some programs require additional datasets or downloaded language/model resources.
- Transformer-based programs may download large pretrained models on their first run and generally require an internet connection.
- Small built-in datasets are intended for demonstration, not as benchmark-quality evaluations.
- Coreference Resolution and document boundary detection use simplified approaches; results depend on the implementation and input data.
- Install dependencies in a virtual environment rather than globally.

## Author

Aditya Mourya
B.Tech CSE (Artificial Intelligence)
Noida Institute of Engineering and Technology (NIET), Greater Noida

---

This repository is maintained for NLP laboratory learning and practice.
