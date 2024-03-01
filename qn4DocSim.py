import string

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def create_bow(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def calculate_similarity(bow1, bow2):

    all_words = set(bow1.keys()).union(set(bow2.keys()))

    dot_product = sum(bow1.get(word, 0) * bow2.get(word, 0) for word in all_words)
    magnitude1 = sum(val ** 2 for val in bow1.values()) ** 0.5
    magnitude2 = sum(val ** 2 for val in bow2.values()) ** 0.5

    # Calculate cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)

# Example usage
def main():
    doc1 = "The Earth orbits around the Sun."
    doc2 = "The Moon orbits around the Earth."
    doc3 = "Mars orbits around the Sun."
    
    doc1 = preprocess_text(doc1)
    doc2 = preprocess_text(doc2)
    doc3 = preprocess_text(doc3)
    
    bow1 = create_bow(doc1)
    bow2 = create_bow(doc2)
    bow3 = create_bow(doc3)
    
    similarity_doc1_doc2 = calculate_similarity(bow1, bow2)
    similarity_doc1_doc3 = calculate_similarity(bow1, bow3)
    
    print("Document 1:", doc1)
    print("Document 2:", doc2)
    print("Document 3:", doc3)
    print("Similarity between doc1 and doc2:", similarity_doc1_doc2)
    print("Similarity between doc1 and doc3:", similarity_doc1_doc3)

if __name__ == "__main__":
    main()
