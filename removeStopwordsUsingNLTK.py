import nltk
from nltk.corpus import stopwords

# Download the stopwords if not already downloaded
nltk.download('stopwords')

# Get the stopwords in English
stop_words = set(stopwords.words('english'))

# Define the input sentence
input_sentence = "This is a sample sentence demonstrating the removal of stopwords."

# Tokenize the sentence into words
words = input_sentence.split()

# Remove the stop words
filtered_words = [word for word in words if word not in stop_words]

# Join the filtered words back into a sentence
filtered_sentence = " ".join(filtered_words)

# Print the filtered sentence
print(filtered_sentence)
