import math
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(doc1, doc2):
    """
    Calculate the cosine similarity between two documents.
    """
    # Convert the documents into word frequency vectors
    doc1_word_freq = Counter(doc1.lower().split())
    doc2_word_freq = Counter(doc2.lower().split())
    
    # Calculate the dot product of the word frequency vectors
    dot_product = sum(doc1_word_freq[word] * doc2_word_freq[word] for word in doc1_word_freq if word in doc2_word_freq)
    
    # Calculate the magnitude of the word frequency vectors
    magnitude_doc1 = math.sqrt(sum([val**2 for val in doc1_word_freq.values()]))
    magnitude_doc2 = math.sqrt(sum([val**2 for val in doc2_word_freq.values()]))
    
    # Calculate the cosine similarity
    cosine_similarity = dot_product / (magnitude_doc1 * magnitude_doc2)
    
    return cosine_similarity

# Example usage
doc1 = "The Earth orbits around the Sun."
doc2 = "The Moon orbits around the Earth."
doc3 = "Mars orbits around the Sun."

similarity_doc1_doc2 = calculate_similarity(doc1, doc2)
similarity_doc1_doc3 = calculate_similarity(doc1, doc3)

print(f"Similarity between doc1 and doc2: {similarity_doc1_doc2}")
print(f"Similarity between doc1 and doc3: {similarity_doc1_doc3}")