import string
news_data = [
    ("Manchester United defeats Liverpool in a thrilling match", "sports"),
    ("New Marvel movie breaks box office records", "entertainment"),
    ("Government announces new tax reforms", "politics"),
    ("Political leaders discuss trade deal", "politics"),
    ("Real Madrid wins the Champions League", "sports"),
    ("New album released by popular band", "entertainment"),
    ("Election results announced by officials", "politics"),
    ("Nadal advances to semi-finals in Wimbledon", "sports"),
    ("Movie premiere attended by Hollywood stars", "entertainment"),
]

def preprocess_text(text):
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    return text.split() 

def build_vocabulary(data):
    vocabulary = set()
    for news_item, _ in data:
        words = preprocess_text(news_item)
        vocabulary.update(words)
    return vocabulary

def calculate_class_priors(data):
    class_counts = {}
    total_count = len(data)
    for _, category in data:
        if category in class_counts:
            class_counts[category] += 1
        else:
            class_counts[category] = 1
    priors = {category: count/total_count for category, count in class_counts.items()}
    return priors

def calculate_word_probabilities(data, vocabulary):
    word_counts = {category: {word: 0 for word in vocabulary} for _, category in data}
    class_counts = {category: 0 for _, category in data}

    for news_item, category in data:
        words = preprocess_text(news_item)
        class_counts[category] += len(words)
        for word in words:
            word_counts[category][word] += 1
    word_probs = {category: {word: (count + 1) / (class_counts[category] + len(vocabulary))
                             for word, count in word_counts[category].items()}
                  for category in class_counts}

    return word_probs

def naive_bayes_classifier(news_item, class_priors, word_probs):
    words = preprocess_text(news_item)
    scores = {category: class_priors[category] for category in class_priors}
    for category in scores:
        for word in words:
            if word in word_probs[category]:
                scores[category] *= word_probs[category][word]

    predicted_category = max(scores, key=scores.get)
    return predicted_category

def main():
    # Test news
    test_articles = [
        "Manchester United triumphs over Liverpool in a gripping showdown, securing victory in sports rivalry.", 
        "New Marvel movie shatters box office records, captivating audiences worldwide.",
        "Government unveils sweeping tax reforms, sparking debates and discussions in politics."
    ]
    # Build vocabulary and calculate probabilities
    vocabulary = build_vocabulary(news_data)
    class_priors = calculate_class_priors(news_data)
    word_probs = calculate_word_probabilities(news_data, vocabulary)
    print("Test Articles Predictions:")
    for article in test_articles:
        predicted_category = naive_bayes_classifier(article, class_priors, word_probs)
        print(f"Article: '{article}'")
        print(f"Predicted Category: {predicted_category}")
        print()

if __name__ == "__main__":
    main()
