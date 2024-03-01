import math
import string

# Define the document collection with IDs
documents = [
    (1, "The quick brown fox jumps over the lazy dog"),
    (2, "The five boxing wizards jump quickly"),
    (3, "Pack my box with five dozen liquor jugs"),
    (4, "How quickly daft jumping zebras vex"),
    (5, "Two driven jocks help fax my big quiz")
]

# Define the query
query = "The quick brown fox jumps over the lazy dog"

# Preprocess the documents and the query
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()
    return words

# Calculate term frequency (TF)
def term_frequency(word, document):
    return document.count(word)

# Calculate document frequency (DF)
def document_frequency(word, documents):
    return sum([word in document for _, document in documents])

# Calculate inverse document frequency (IDF)
def inverse_document_frequency(word, documents):
    return math.log(len(documents) / (1 + document_frequency(word, documents)))

# Calculate TF-IDF
def tf_idf(word, document, documents):
    tf = term_frequency(word, document)
    idf = inverse_document_frequency(word, documents)
    return tf * idf

# Create a TF-IDF matrix for all words in all documents
def create_tf_idf_matrix(documents):
    tf_idf_matrix = {}
    for _, document in documents:
        for word in preprocess(document):
            if word not in tf_idf_matrix:
                tf_idf_matrix[word] = [tf_idf(word, document, documents) for _, document in documents]
    return tf_idf_matrix

# Create the TF-IDF matrix
tf_idf_matrix = create_tf_idf_matrix(documents)

# Create the query vector
query_vector = [tf_idf(word, query, documents) for word in tf_idf_matrix.keys()]

# Calculate the cosine similarity between the query vector and each document vector
def cosine_similarity(query_vector, document_vector):
    dot_product = sum(q * d for q, d in zip(query_vector, document_vector))
    magnitude_query = math.sqrt(sum(q ** 2 for q in query_vector))
    magnitude_document = math.sqrt(sum(d ** 2 for d in document_vector))
    return dot_product / (magnitude_query * magnitude_document)

# Print the cosine similarity for each document
print("Cosine Similarity:")
for doc_id, document in documents:
    document_vector = [tf_idf(word, document, documents) for word in tf_idf_matrix.keys()]
    cosine_similarity_value = cosine_similarity(query_vector, document_vector)
    print(f"Cosine for Document {doc_id} is {cosine_similarity_value:.2f}")

# Print the document matching the query
print("\nMatching Document:")
matching_document = max(documents, key=lambda x: cosine_similarity(query_vector, [tf_idf(word, x[1], documents) for word in tf_idf_matrix.keys()]))
print(f"Document {matching_document[0]}: {matching_document[1]}")
