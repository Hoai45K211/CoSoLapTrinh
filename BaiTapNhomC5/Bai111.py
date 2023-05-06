def get_words(sentence):
    punctuations = ',.?-\'`!:;'
    words = [word.strip(punctuations) for word in sentence.split()]
    return words

def main():
    sentence = input('Enter your sentence:')
    word_list = get_words(sentence)
    print(word_list)
    
main()