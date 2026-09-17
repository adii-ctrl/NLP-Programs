# NLP Unit 1 Programs

This repository contains the Unit 1 programs for Natural Language Processing (NLP), implemented using Python, NLTK, and spaCy.

## About the Project

The purpose of these programs is to understand and implement fundamental Natural Language Processing techniques such as tokenization, stemming, lemmatization, stop-word removal, POS tagging, parsing, chunking, and named entity recognition.

## Technologies Used

* Python 3.11
* NLTK
* spaCy
* Regular Expressions (RegEx)
* VS Code

## Programs Included

### 1. Tokenization

**Folder:** `01_Tokenization`

Tokenization divides a text into smaller units such as sentences and words.

This program demonstrates:

* Sentence tokenization using NLTK
* Word tokenization using NLTK
* Sentence tokenization using spaCy
* Word tokenization using spaCy

### 2. Stemming and Lemmatization

**Folder:** `02_Stemming_Lemmatization`

This program demonstrates two techniques for reducing words to their base or root forms.

* Stemming using Porter Stemmer
* Lemmatization using WordNet Lemmatizer

### 3. Stop-word Removal

**Folder:** `03_Stopword_Removal`

This program removes common words such as "is", "the", "a", "of", and "it" from a document using NLTK stop-word lists.

### 4. Part-of-Speech Tagging

**Folder:** `04_POS_Tagging`

This program assigns grammatical tags to words in a sentence, such as:

* Noun
* Verb
* Adjective
* Adverb
* Determiner

### 5. Parsing and Chunking

**Folder:** `05_Parsing_Chunking`

This program demonstrates:

* Regular Expression based chunking using NLTK
* Dependency parsing using spaCy

### 6. Named Entity Recognition

**Folder:** `06_NER`

This program uses spaCy to identify named entities in text, such as:

* Person
* Organization
* Location
* Date

## Project Structure

```text
NLP-Unit-1-Programs/
│
├── 01_Tokenization/
│   └── tokenization.py
│
├── 02_Stemming_Lemmatization/
│   └── stemming_lemmatization.py
│
├── 03_Stopword_Removal/
│   └── stopword_removal.py
│
├── 04_POS_Tagging/
│   └── pos_tagging.py
│
├── 05_Parsing_Chunking/
│   └── parsing_chunking.py
│
├── 06_NER/
│   └── named_entity_recognition.py
│
├── README.md
└── requirements.txt
```

## Installation

Create and activate a Python virtual environment:

```bash
python -m venv venv
```

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Install the spaCy English language model:

```bash
python -m spacy download en_core_web_sm
```

## How to Run

Run any program from the project root directory.

Example:

```bash
python .\01_Tokenization\tokenization.py
```

Other programs can be executed similarly.

## Learning Outcomes

After completing these programs, the following NLP concepts are demonstrated:

* Text tokenization
* Word normalization
* Stop-word removal
* Grammatical analysis
* Phrase chunking
* Dependency parsing
* Named entity recognition

## Author

**Aditya Mourya**

B.Tech Computer Science and Engineering (Artificial Intelligence)
