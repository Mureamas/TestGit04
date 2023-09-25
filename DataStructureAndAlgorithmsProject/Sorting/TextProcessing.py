import re
from collections import Counter

def text_processing(text):
    # Tokenize the text by splitting it into words (tokens)
    tokens = re.findall(r'\b\w+\b', text.lower())

    # Calculate word frequency using Counter
    word_frequency = Counter(tokens)

    return word_frequency
