def censor_words(sentence, bad_words):
    words = sentence.split()
    for i, word in enumerate(words):
        if word.lower() in bad_words:
            words[i] = '*' * len(word)
    return ' '.join(words)
    
sentence = "This is a bad and dumb example of a terrible sentence."
bad_words = ["bad", "dumb", "terrible"]
filtered_sentence = censor_words(sentence, bad_words)
print(filtered_sentence)
