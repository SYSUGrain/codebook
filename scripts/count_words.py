import collections
import re

def count_words(text):
    """Split words on spaces."""
    counts = collections.defaultdict(int)
    words = re.sub(r"\s+", " ", text.lower()).split(' ')
    for word in words:
        counts[word] += 1
    return counts

def count_words_in_file(in_file, out_file):
    with open(in_file, 'r') as f:
        counts = count_words(f.read())

    with open(out_file, 'w') as f:
        for word, count in counts.items():
            f.write(f"{word},{count}\n")
