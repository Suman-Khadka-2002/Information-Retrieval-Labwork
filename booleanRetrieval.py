# A simple dictionary to represent the documents
documents = {
    1: "English tutorial and fast track",
    2: "Book on semantic analysis",
    3: "Learning latent semantic indexing",
    4: "Advance in structure and semantic indexing",
    5: "Analysis of latent structures"
}

# A dictionary to store the inverted index
inverted_index = {}

# Populate the inverted index
for doc_id, text in documents.items():
    for word in text.split():
        if word not in inverted_index:
            inverted_index[word] = set()
        inverted_index[word].add(doc_id)

# The query
query = "advance AND structure AND NOT analysis”"

# Parse the query
query_terms = query.split()
query_sets = []
current_set = set()
for term in query_terms:
    if term == "and":
        query_sets.append(current_set)
        current_set = set()
    elif term == "or":
        query_sets.append(current_set)
        current_set = set()
    elif term in inverted_index:
        current_set.update(inverted_index[term])
else:
    query_sets.append(current_set)

# Intersection of query sets
result_set = query_sets[0]
for i in range(1, len(query_sets)):
    result_set = result_set.intersection(query_sets[i])

# Get the document ids from the result set
document_ids = list(result_set)

# Print the result
print("Documents matching the query:")
for doc_id in document_ids:
    print(f"Document {doc_id}: {documents[doc_id]}")