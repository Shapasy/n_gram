path = "./data_set.txt"

import nltk
# import numpy as np

def fetch_data_set():
    with open(path, "r",encoding='utf-8') as f:
        data = f.read()
    return data

def tokenize_data_set(data):
    sentences  =  data.split('\n')
    
    sentences_len = len(sentences)
    
    new_sentences = []
    
    for i in range(sentences_len):
        sentence = sentences[i]
        if(len(sentence) > 0):
            sentence = sentence.strip()
            sentence = sentence.lower()
            sentence = nltk.word_tokenize(sentence)
            new_sentences.append(sentence)   
        if(i%int(sentences_len/3) == 0 and i != 0):
            print(f"{int((i/sentences_len)*100)}% tokenized 🎈")
    print("100% tokenized 🎈")       
    return new_sentences

def count_words(tokenized_sentences,count_threshold=2):
    print("Counting the words in the data set 🎈🎈")
    word_counts = {}
    
    for sentence in tokenized_sentences:
        for token in sentence:
            if(token not in word_counts.keys()):
                word_counts[token] = 0
            word_counts[token] +=1

    print(f"Removing low frequency word from the data set 🎈🎈")
    word_counts_2 = {}
    
    for word,cnt in word_counts.items():
        if cnt >= count_threshold: 
            word_counts_2[word] = cnt
      
    return word_counts_2

def fetch_preprocessed_data_set():
    print("Start preprocessing the data 🎈🎈🎈")
    data = fetch_data_set()
    tokenized_sentences = tokenize_data_set(data)
    word_counts = count_words(tokenized_sentences)
    print("Finished preprocessing the data 🎈")
    return tokenized_sentences, word_counts

# def split_train_test_sets(tokenized_sentences,train_set_ratio):
#     if(train_set_ratio < 0.01 or train_set_ratio >= 1): return
#     np.random.seed(99)
#     np.random.shuffle(tokenized_sentences)
#     train_size = int(len(tokenized_sentences) * train_set_ratio)
#     train_data = tokenized_sentences[0:train_size]
#     test_data = tokenized_sentences[train_size:]
#     return train_data, test_data

def get_data():
    tokenized_sentences, word_counts = fetch_preprocessed_data_set()
    # train_data, test_data = split_train_test_sets(tokenized_sentences,train_set_ratio)
    return tokenized_sentences , word_counts

#--------------------------------------------------------
# if __name__ == "__main__":
#     train_data, test_data, word_counts = get_data(train_set_ratio=0.8)
#     print(len(train_data))
#     print(len(test_data))
#     print(word_counts)
    
    
    
