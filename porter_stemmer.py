import nltk
from nltk.stem import PorterStemmer

# Initialize Porter Stemmer
porter = PorterStemmer()

# Sample words
words = ["caresses", "flies", "dies", "mules", "denied", "died", "agreed", "owned", 
         "humbled", "sized", "meeting", "stating", "itemization", "sensational", "traditional"]

# Stemming
stemmed_words = [porter.stem(word) for word in words]
print('the stemmed data are')
# Print original and stemmed words
for original, stemmed in zip(words, stemmed_words):
    print(original, '->', stemmed)