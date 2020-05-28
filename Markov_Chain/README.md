# Outline:

- In mathematical terms, a Markov Chain is a model that outlines an outcome or a sequence of events where the probability of each event depends solely on the previous event. In terms of text processing, a Markov Chain is used to generate random sentences from some corpus of words. A more detailed description of how it works is presented below.

# Purpose:

- The project helped introduce me to a very important and useful mathematical model that is used very commonly in dealing with data and predicting events. While what I have built presently only scrapes the tip of the Markovian iceberg, I am extremely excited to research it more and use it in other projects!

# Description:

- The build turned out to be a lot easier than I had originally thought it would. I used a portion of the script of Shrek that I found on reddit as my corpus of words and first split it and stored all the words.
- Then using a generator, I converted all the words to pairs as tuples and then using a defaultdict, I sorted the words into a dictionary where the key is a word and the values are all the words that have followed it at some point in the text.
- Finally, I chose a random word from the list of words and chose a random word from the words that followed it using the dictionary as indicated above, repeating this process for a set number of times.
    ```python
    for i in range(num_words):
            chain.append(np.random.choice(pair_dict[chain[-1]]))
    ```
- This approach is not strictly Markovian as it does not make use of the probabilities of words pairs and I am currently working on implementing that facet.
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

- Inspiration for this project came from Ben Shaver on Medium!
