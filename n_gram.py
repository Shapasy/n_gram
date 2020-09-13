def count_n_grams(sentences, n, start_token='<s>', end_token = '<e>'):
    n_grams = {}
     
    for sentence in sentences: 
        sentence = [start_token]*n + sentence + [end_token]
        sentence = tuple(sentence)
            
        m = len(sentence) if n==1 else len(sentence)-1
        for i in range(m): 
            n_gram = sentence[i:i+n]

            if n_gram not in n_grams.keys(): n_grams[n_gram] = 0
            n_grams[n_gram] +=1
             
    return n_grams


def estimate_probability(word, previous_n_gram, 
                         n_gram_counts, n_plus1_gram_counts, vocabulary_size, k=1.0):
    
    previous_n_gram = tuple(previous_n_gram) 
    
    previous_n_gram_count = n_gram_counts[previous_n_gram] if previous_n_gram in n_gram_counts  else 0
    
    denominator = previous_n_gram_count + k * vocabulary_size

    n_plus1_gram = previous_n_gram + (word,)

    n_plus1_gram_count = n_plus1_gram_counts[n_plus1_gram] if n_plus1_gram in n_plus1_gram_counts  else 0

    numerator = n_plus1_gram_count + k

    probability = numerator / denominator
    
    return probability

def estimate_probabilities(previous_n_gram, n_gram_counts, n_plus1_gram_counts, vocabulary, k=1.0):
    previous_n_gram = tuple(previous_n_gram)
    
    vocabulary = vocabulary + ["<e>", "<unk>"]
    vocabulary_size = len(vocabulary)
    
    probabilities = {}
    for word in vocabulary:
        probability = estimate_probability(word, previous_n_gram, 
                                           n_gram_counts, n_plus1_gram_counts, 
                                           vocabulary_size, k=k)
        probabilities[word] = probability

    return probabilities


def suggest_a_word(previous_tokens, n_gram_counts, n_plus1_gram_counts, vocabulary, k=1.0, start_with=None):
    n = len(list(n_gram_counts.keys())[0]) 

    previous_n_gram = previous_tokens[-n:]

    probabilities = estimate_probabilities(previous_n_gram,
                                           n_gram_counts, n_plus1_gram_counts,
                                           vocabulary, k=k)
    suggestion = None
    max_prob = 0

    for word, prob in probabilities.items():
        if start_with != None: 
            if not word.startswith(start_with): continue 
        if prob > max_prob:
            suggestion = word
            max_prob = prob
    
    return suggestion, max_prob




