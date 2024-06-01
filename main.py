import pandas as pd
from collections import Counter


def print_basic_statistics(csv_file_path):
    df = pd.read_csv(csv_file_path, encoding='latin-1')
    df.columns = ['v1', 'v2', 'v3', 'v4', 'v5']

    total_messages = df.shape[0]

    spam_count = df[df['v1'] == 'spam'].shape[0]
    ham_count = df[df['v1'] == 'ham'].shape[0]

    df['word_count'] = df['v2'].apply(lambda x: len(x.split()))
    avg_words_per_message = df['word_count'].mean()

    all_words = ' '.join(df['v2']).split()
    most_common_words = Counter(all_words).most_common(5)

    word_counts = Counter(all_words)
    words_once = sum(1 for count in word_counts.values() if count == 1)

    print(f'Total number of SMS messages: {total_messages}')
    print(f'Number of spam messages: {spam_count}')
    print(f'Number of ham messages: {ham_count}')
    print(f'Average number of words per message: {avg_words_per_message:.2f}')
    print('5 most frequent words:', most_common_words)
    print(f'Number of words that only appear once: {words_once}')


print_basic_statistics('spam.csv')
