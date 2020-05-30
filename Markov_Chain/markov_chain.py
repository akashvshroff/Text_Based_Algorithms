from collections import defaultdict
import random


def get_end_words(words):
    end_words = []
    for word in words:
        if word[-1] in ['.', '?', '!'] and len(word) != 1:
            end_words.append(word)
    return end_words


def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])


def create_list(pairs):
    pair_list = []
    for lead, trail in pairs:
        pair_list.append((lead, trail))
    return pair_list


def check_frequency(words, pair_list, pair_dict):
    unique_pairs = set(pair_list)
    for pair in unique_pairs:
        count_pair = pair_list.count(pair)
        lead, trail = pair[0], pair[1]
        count_word = words.count(lead)
        probability = count_pair/count_word
        pair_dict[lead].append([trail, probability])

    return pair_dict


def make_random_choice(trails):
    if len(trails) == 1:
        return trails[0][0]
    else:
        words = [x for [x, y] in trails]
        weights = [y for [x, y] in trails]
        return random.choices(words, weights, k=1)[0]


def generate_sentence(words, pair_dict, num_words):
    first_word = random.choice(words)
    while first_word.islower() or not first_word.isalpha():
        first_word = random.choice(words)
    chain = [first_word]
    for i in range(num_words):
        curr_word = chain[-1]
        trail_words = pair_dict[curr_word]
        if not trail_words:
            trail_words = pair_dict[chain[-2]]
        chain.append(make_random_choice(trail_words))
    return chain


def main():
    shrek = open(
        r'C:\Users\akush\Desktop\Programming\Projects\Text_Based_Algorithms\Markov_Chain\shrek_script.txt', encoding='utf8').read()
    words = shrek.split()
    pairs = make_pairs(words)
    end_words = get_end_words(words)
    pair_dict = defaultdict(list)
    pair_list = create_list(pairs)
    pair_dict = check_frequency(words, pair_list, pair_dict)
    num_words = 50
    word_gen = generate_sentence(words, pair_dict, num_words)
    if word_gen[-1] not in end_words:
        word_gen.append(random.choice(end_words))
    print(' '.join(word_gen))


if __name__ == '__main__':
    main()
