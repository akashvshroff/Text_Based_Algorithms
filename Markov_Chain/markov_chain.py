import numpy as np
from collections import defaultdict


def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])


def create_dict(pairs, pair_dict):
    for word1, word2 in pairs:
        pair_dict[word1].append(word2)
    return pair_dict


def generate_sentence(words, pair_dict, num_words):
    first_word = np.random.choice(words)
    while first_word.islower() or not first_word.isalpha():
        first_word = np.random.choice(words)
    chain = [first_word]
    for i in range(num_words):
        chain.append(np.random.choice(pair_dict[chain[-1]]))
    return chain


def main():
    shrek = open(
        r'C:\Users\akush\Desktop\Programming\Projects\Text_Based_Algorithms\Markov_Chain\shrek_script.txt', encoding='utf8').read()
    words = shrek.split()
    pairs = make_pairs(words)
    pair_dict = defaultdict(list)
    pair_dict = create_dict(pairs, pair_dict)
    num_words = 25
    word_gen = generate_sentence(words, pair_dict, num_words)
    print(' '.join(word_gen))


if __name__ == '__main__':
    main()
