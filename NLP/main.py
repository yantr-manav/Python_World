import nltk
# nltk.download('punkt')  # only 'punkt' is needed for sent_tokenize

from nltk.tokenize import sent_tokenize

corpus = """Hello, how are you doing today? The weather is great, and Python is awesome. The sky is blue and the sun is shining."""

sentences = sent_tokenize(corpus)
print(sentences)

