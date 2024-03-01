import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")

# Initialize the stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Initialize the stop word list
stop_words = set(stopwords.words("english"))

# Define the paragraph
paragraph = "The quick brown fox jumps over the lazy dog, while the sun sets behind the tall, majestic mountains. The birds chirp as the day comes to an end, and the stars begin to twinkle in the sky. The night is peaceful, and the world is still."

# Perform lowercasing
lowercased_paragraph = paragraph.lower()
print("After performing Lowercasing :")
print(lowercased_paragraph)
print()

# Perform tokenization
tokenized_paragraph = lowercased_paragraph.split()
print("After Tokenization:")
print(tokenized_paragraph)
print()

# Perform stemming
stemmed_paragraph = []
for word in tokenized_paragraph:
    stemmed_paragraph.append(stemmer.stem(word))
print("After Stemming:")
print(stemmed_paragraph)
print()

# Perform punctuation removal
punctuation_removed_paragraph = [
    word.strip(string.punctuation)
    for word in stemmed_paragraph
    if word.strip(string.punctuation)
]
print("After Punctuation removal:")
print(punctuation_removed_paragraph)
print()

# Perform stop words removal
stop_words_removed_paragraph = [
    word for word in punctuation_removed_paragraph if word not in stop_words
]
print("After Stopwords removal:")
print(stop_words_removed_paragraph)
print()

# Perform lemmatization
lemmatized_paragraph = []
for word in stop_words_removed_paragraph:
    lemmatized_paragraph.append(lemmatizer.lemmatize(word))
print("After Lemmatization:")
print(lemmatized_paragraph)
