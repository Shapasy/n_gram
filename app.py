import nltk

from preprocessing import get_data
from n_gram import count_n_grams,suggest_a_word

if __name__ == "__main__":
    tokenized_sentences , word_counts = get_data()
    
    print("building n-gram model 🚀🚀")
    unique_words = list(word_counts.keys())
    unigram_counts = count_n_grams(tokenized_sentences, 1)
    bigram_counts = count_n_grams(tokenized_sentences, 2) 
    print("Finshed building the model 🎯")
    
    print("Some results from the model 👀 :-")
    texts = ["how","i like","you","please","i need","give me your","allow us to"] 
    for text in texts:
        previous_tokens = nltk.word_tokenize(text)
        
        suggestion, max_prob = suggest_a_word(previous_tokens,
        unigram_counts, bigram_counts, unique_words, k=1.0)
        
        print("Text :",text)
        print("Suggestion :",suggestion)
        # print(f"Suggestion : {suggestion} -> {int(max_prob*100)}%")
        print("----------------------------------")
    
    
    
    
    
