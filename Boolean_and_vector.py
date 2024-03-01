import math

# Sample documents
documents = {
    'doc1': 'apple orange banana',
    'doc2': 'apple banana mango',
    'doc3': 'orange banana grape',
    'doc4': 'banana mango grape',
    'doc5': 'apple mango grape'
}

# Tokenize documents
tokenized_documents = {doc_id: document.split() for doc_id, document in documents.items()}

# Boolean Retrieval Model
def boolean_search(query, documents):
    results = []
    for doc_id, document in documents.items():
        if all(term in document for term in query):
            results.append(doc_id)
    return results

# Vector Space Model
def tf(term, document):
    return document.count(term)

def idf(term, documents):
    N = len(documents)
    df = sum(term in document for document in documents.values())
    return math.log10(N/df)

def tf_idf(term, document, documents):
    return tf(term, document) * idf(term, documents)

def cosine_similarity(query, document, documents):
    query_vector = [tf_idf(term, query, documents) for term in query]
    document_vector = [tf_idf(term, document, documents) for term in query]

    dot_product = sum(q * d for q, d in zip(query_vector, document_vector))
    query_norm = math.sqrt(sum(q**2 for q in query_vector))
    document_norm = math.sqrt(sum(d**2 for d in document_vector))

    return dot_product / (query_norm * document_norm)

def vector_space_search(query, documents):
    results = []
    for doc_id, document in documents.items():
        similarity = cosine_similarity(query, document, documents)
        results.append((doc_id, similarity))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# Example queries
boolean_query = ['apple', 'banana']
vector_space_query = ['apple', 'banana', 'mango']

# Boolean Retrieval Model
print("Boolean Retrieval Model:")
boolean_results = boolean_search(boolean_query, tokenized_documents)
print("Results for query", boolean_query, ":", boolean_results)

# Vector Space Model
print("\nVector Space Model:")
vector_space_results = vector_space_search(vector_space_query, tokenized_documents)
print("Results for query with the cosine similarity", vector_space_query, ":\n", vector_space_results)