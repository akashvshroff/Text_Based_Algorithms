# Outline:

- In mathematical terms, a Markov Chain is a model that outlines an outcome or a sequence of events where the probability of each event depends solely on the event that precedes it. In terms of text processing, a Markov Chain is used to generate random sentences from some corpus of words based on probability of pairs. A more detailed description of how it works is presented below.

# Purpose:

- The project helped introduce me to a very important and useful mathematical model that is used very commonly in dealing with data and predicting events. While what I have built presently only scrapes the tip of the Markovian iceberg, I am extremely excited to research it more and use it in other projects!

# Description:

- The build turned out to be a lot easier than I had originally thought it would. I used a portion of the script of Shrek that I found on reddit as my corpus of words and first split it and stored all the words.
- Then using a generator, I converted all the words to pairs as tuples and then created a set of all the tuples, analysing the probability of a leading word being followed by a trailing word by analysing the number of times it occurs versus the number of times the leading word occurs in the corpus of words.
    ```python
    def check_frequency(words, pair_list, pair_dict):
        unique_pairs = set(pair_list)
        for pair in unique_pairs:
            count_pair = pair_list.count(pair)
            lead, trail = pair[0], pair[1]
            count_word = words.count(lead)
            probability = count_pair/count_word
            pair_dict[lead].append([trail, probability])

        return pair_dict
    ```
- These values are appended to a defaultdict, where the key is the leading word and the value is a list of lists where each list holds a trailing word and the probability of it's occurence.
- I wrote another function that chose a random word from a set of trailing words by using the random.choices function and using the probability of occurence as the weights for the choice.
    ```python
    def make_random_choice(trails):
        if len(trails) == 1:
            return trails[0][0]
        else:
            words = [x for [x, y] in trails]
            weights = [y for [x, y] in trails]
            return random.choices(words, weights, k=1)[0]
    ```
- Finally, I chose a random word from the list of words and chose a random word from the words that followed it (through the above function), repeating this process for a set number of times.
    ```python
    for i in range(num_words):
          curr_word = chain[-1]
          trail_words = pair_dict[curr_word]
          if not trail_words:
              trail_words = pair_dict[chain[-2]]
          chain.append(make_random_choice(trail_words))
    ```
- The program also ascertains certain end-words to make sure that the generated text does not run off midway and if the text does not end with the end word, one is randomly assigned to it.
    ```python
    def get_end_words(words):
        end_words = []
        for word in words:
            if word[-1] in ['.', '?', '!'] and len(word) != 1:
                end_words.append(word)
        return end_words
    ```
- I ensured that the first word was not lowercase or any set of numbers or awry punctuation using the following bit of code:
    ```python
    while first_word.islower() or not first_word.isalpha():
            first_word = np.random.choice(words)
    ```
- A random (seemingly bipolar) outcome that this program generated is:
  - They thought you'd understand? Oh, good. Hey. Come on road again. Just the people, you up there? Well, maybe even love this romantic. Just let me that. So you both of all right? Right? -Donkey. -No! Ok, fine. Attention all the matter to be our champion! What? Congratulation, Ogre. You've chosen...
- Inspiration for this project came from Towards Data Science on Medium!
