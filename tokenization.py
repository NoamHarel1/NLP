import pandas as pd
import nltk
import time
from nltk.tokenize import word_tokenize
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

nltk.download('punkt')


def tokenize_nltk(text):
    return word_tokenize(text)


def tokenize_spacy(text):
    nlp = English()
    tokenizer = Tokenizer(nlp.vocab)
    tokens = tokenizer(text)

    return list(tokens)


def analyze_tokenization_time(df, tokenizer, tokenizer_name):
    start_time = time.time()
    col_name = f'{tokenizer_name}_tokens'
    df[col_name] = df['v2'].apply(tokenizer)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tokenization with {tokenizer_name} took {elapsed_time:.4f} seconds")


def load_data_and_tokenize(csv_file_path):
    df = pd.read_csv(csv_file_path, encoding='latin-1')
    df.columns = ['v1', 'v2', 'v3', 'v4', 'v5']

    analyze_tokenization_time(df, tokenize_nltk, 'nltk')

    analyze_tokenization_time(df, tokenize_spacy, 'spaCy')

    print(df[['v2', 'nltk_tokens', 'spaCy_tokens']].head())


load_data_and_tokenize('spam.csv')
