# Outline:

- This segment of the text-based algorithms contain programs that run based on the principles of hashing. These programs, that tackle common string-based problems and form the backbone of modern string processing, are slightly more complex to wrap your head around at first owing to the multitude of new concepts but I shall try to break them down as simply as I can in the detailed description below!

# Purpose:

- I was introduced to the concept of using hashing to solve string-based programs through the Data Structures course in my Data Structures and Algorithms specialisation on Coursera offered by UCSD and HSE while we were tackling the implementation of hash-tables and the general concept of hashing.
- Hashing forms the backbone of modern computing (literally any mapping on any system uses hashing!) and has a number of applications in emerging areas too - Blockchain being one of them and string processing another and therefore I was immensely excited to understand its advantages and how to properly implement such a system.
- As mentioned above, hashing takes some time to wrap your head around as you can't often visualise a hash as you can a string or integer and while it took to me a number of Stackoverflow searches to arrive at some of these solutions, it was well worth it and now I am much better equipped to deal with a certain kind of problem! I hope I can explain this concept just as well.

# Description:

- I realise hashing sounds quite complex and seems like voodoo but let me try to break it down for you.
- First off, have you ever used a dictionary in the programming language of your choice? Well if yes, then congrats because you have unknowingly been using hashing for quite some time! (If no then maybe this post isn't for you... unless you've vowed never to use a dictionary in your life - then maybe you're welcome.)
- To help you understand hashing and these programs, I want to define a few things and explain some ideas and then you'll be able to understand how the concepts have been used to solve the programs!

### What is hashing anyway?
- Hashing, quite simply put, is the process of converting a 'key' (it can be any object of any length) into a fixed-length value called a hash through some form of expression (usually mathematic).
- Now certain ideas pop out. A key can realistically be any object but for now, we will consider a string since that is what we are dealing with mainly. To convert a key into a hash, you have to make a deterministic conversion, i.e the hashing algorithm can only convert a particular key to a particular hash (but many keys can have the same hash - we'll cover this). Therefore a hash cannot be random.
- To illustrate this, consider a simple hashing algorithm where keys are converted to their ASCII value, summed and the sum is then taken mod 20 (If you are unfamiliar with modular arithmetic or do not remember it, please take a refresher [here](https://brilliant.org/wiki/modular-arithmetic/) since I refer to it a lot!)
- The string "ABC" would therefore be (65+66+67)%20 which is 198%20 which is finally 18. While the string "ABCDBSDBBEHWBEWHEB" would be 12 (take my word for it...). Using such a procedure, any string can be converted to a number from 0 to 19. A side note: if we have we want to store only strings as keys, we have successfully implemented a basic version of a dictionary! We can maintain an array of size 20 and therefore for any key, you can convert it to an index position and store a value at the corresponding position! Any conversion therefore cannot be random since you want to be able to access the same index!
- Now there are glaring issues with our implementation but one such error stands out - look at the string "ABC" and the string "UVW". Using this procedure, we get the same hash value - 18. This is called a **collision**.

### What is a collision?
- A collision is a situation where 2 keys that are not equal, have the same hash and this can lead to some problems but can be well avoided by choosing a better hash function (Here I thought my simple hash function was enough...)
- Above I discussed using hashing to implement a dictionary but a dictionary has to be built to account for collisions - this can be done by storing a tuple of (key, value) in a list at the index position instead of storing just the value. Therefore in case of a collision, the tuple can simply be appended to the end of the list at the index position and to find a key, you can scan the list at the index position and match the key. Thus, it is very important to ensure that you get a dictionary with relatively fast look-ups, you have you craft a hash-function that can evenly distribute hashes across the indices and doesn't simply hash everything to the same value.

### What is a good hash?

- Now, rather than delving into the theory behind what makes a good hashing function and the concept of a universal family of hashes, I want to show you the two hashing algorithms that I've used in these programs, both polynomial hashes, where a large prime (greater than length of input string) and constant multiplier are used to minimise collisions to a probability of n/m where n is the length of the input and m is the prime number (read about it more [here.](https://cp-algorithms.com/string/string-hashing.html))

- The first hash I employed is as follows:

    ```python
    def poly_hash(s, P, X):
        """
        Hash a string using a polynomial hashing function that uses a large prime
        number (P) and a multiplier (X). The hashing uses the ascii code of each
        letter.
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * X + ord(c)) % P
        return ans
    ```

    - This function is simply the summation of the characters of the string in ascii*X (multiplier) and at each step the hash is taken mod P (large prime) in order to ensure the hash does not get too big.
    - Mathematically, this is represented as:

        ![alt-text](https://github.com/akashvshroff/Text_Based_Algorithms/blob/master/Hashing_Based/Equations/h1.svg)

    - Where n is the length of the string s.
- The second hash function that I employed was:

    ```python
    def hash_function(s, X, P):
        """
        Taking a string s, return its hash value by using a hash function where
        for a string s(s0,s1...sm-1) i.e of length m, the hash is a sum of s[j]*X(m-j-1)
        for j from 0 to m-1.
        """
        ans = 0
        m = len(s)
        for j in range(m):
            ans = (ans + ord(s[j])*pow(X, m-j-1)) % P
        return ans
    ```

    - This hash function looks slightly more complex, but it really isn't, the only difference is the fact that the multiplier is taken as an exponent to the power of the length of the remaining chars, therefore going from m-1 to 0.
    - Again, mathematically, this is:

        ![alt-text](https://github.com/akashvshroff/Text_Based_Algorithms/blob/master/Hashing_Based/Equations/h2.svg)

    - Where m is the length of the string s.

    - Now since I have shown you the hash functions that I used, let me show you why I used them and the one key feature that makes hashing so powerful.

### Rolling hash functions:
- Presently, the advantage of using hashes in our programs isn't quite apparent yet, it seems like the same if not more work. You see, the key benefit of using hashes comes when you consider the idea of a **rolling hash**. A rolling hash is honestly just a fancier way of saying that you can calculate the hash for a particular substring or string using a hash value that you've already computed.
- So why do we care about this? Well, it means that once we've calculated some initial hash, we can calculate the rest of the hashes in almost **constant time O(1).** Now that is something that is very alluring and key to our programs (especially in the Rabin-Karp algorithm).
- You may be wondering how our present hashes can be converted into a rolling hash, well let me show you using our first hashing algorithm. (Excuse my handwriting - I have also not considered the modulo prime since it remains the same).

![alt-text](https://github.com/akashvshroff/Text_Based_Algorithms/blob/master/Hashing_Based/Equations/rolling_hash_1.jpg)

- Now given our first hashing algorithm, we can see that the hash of any substring actually depends on the hash of the substring after it and therefore, if we move from the end back to the beginning, for any H(i) we can calculate it in constant time provided we have H(i+1). Note, since our strings are 0-based, it would be S[i-1]. You can see the rolling hash code here:

    ```python
    def precompute_hashes(T, len_p, P, X):
        """
        Precompute the required hashes of substrings of length len_p in T in
        constant time using the hash of the next substring.
        """
        len_t = len(T)
        H = [0 for _ in range(len_t-len_p+1)]
        S = T[len_t-len_p:len_t]
        H[len_t-len_p] = poly_hash(S, P, X)
        y = pow(X, len_p, P)
        for i in range(len_t-len_p-1, -1, -1):
            H[i] = (X * H[i+1] + ord(T[i]) - y * ord(T[i+len_p])) % P
        return H
    ```
    - Here we precompute the hashes in constant time using the end hash S in text T so we can easily compare hashes.

- The very same idea is employed in the other hashing function and this relation is used to generate a neat rolling hash function like so:

    ```python
    def pre_process_string(s):
        """
        Preprocess the string and get 2 hash-tables using which you can compute the
        hashes of 2 substrings in constant time. We use 2 hash-tables to lower the
        probability that there is a collision (i.e same hash but diff substring) to
        a very negligible amount (n/m where n is the lenght of the substring and m
        is the prime number with which you take modulus.)
        """
        n = len(s)
        base = pow(10, 9)
        M1 = base+7
        M2 = base+9  # i.e 10**9 + 9
        # X = random.randint(1, base)
        X = 263
        h1 = [0 for _ in range(n+1)]
        h2 = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            h1[i] = (X*h1[i-1] + ord(s[i-1])) % M1
            h2[i] = (X*h2[i-1] + ord(s[i-1])) % M2
        return X, h1, h2, M1, M2

    def hash_value(table, prime, x, start, length):
        y = pow(x, length, prime)
        hash_value = (table[start+length] - y*table[start]) % prime
        return hash_value
    ```
    - Here we precompute a table of all the hash-values so far using our hashing function in the pre_process_string function and then in the hash_value function, we use a rolling hash relation in order to ascertain the required hash!

- We are now done with all our pre-processing and now know enough to understand the approaches required to solve the programs!

## The Programs:

### Note:

- It is important to note that all the programs use either a second prime number and multiplier or an additional equality check in order to make certain that the strings are equal and it is not a collision.

### Rabin-Karp Pattern Matching:

- The Rabin-Karp pattern matching algorithm succinctly uses hashing to return the starting positions of every occurrence of a pattern in a text. For example, with the text 'ABCDEBCDHEURBCD' and the pattern 'BCD', the algorithm would return 1,5,12 - 0-based values for the starting index of the pattern in the string.
- The naïve algorithm for this, without the use of hashing, can solve it in O(nm) time where n is the length of the text and m is the length of the pattern. This Rabin Karp algorithm solves it in O(n+m) in the best and average case while O(nm) for the worst case (this case would only occur with a very bad hash function that leads to a collision or false-positive at each step).
- The program uses the first hash function and its corresponding rolling hash function to precompute the hashes for all possible candidates of the matching substring from i = 0 to m-n+1. It then checks the hash of the pattern against the pre-computed hash of the substring and in case there is a match, it checks the substring against the pattern as an added measure of safety (this can be avoided by using multiple prime numbers and 2 hashing functions). In case they match, it appends i to the list of found indices and returns the list once all candidates have been found.
- Read more about the algorithm [here!](https://brilliant.org/wiki/rabin-karp-algorithm/)

### Substring Equality:
- This program takes in one string and 3 inputs (start1,start2,length) and it outputs Yes if the substring from start1 till start1+length is equal to the substring from start2 to start2 + length. Instead of constantly splicing the string and checking for equality, using the second hashing algorithm and subsequent rolling hash, we can pre-process the string and generate a hash table from which we can obtain the hash-value for any substring in constant time.
- We pre-process the string into 2 hash-tables in order to further minimize the chances of collisions and match the hashes twice and output 'Yes' if they match, else 'No'.
- This program effectively displays the power of hashing in massively reducing the time it takes to solve a program.

### Longest Common Substring:
- This program is slightly more complex and given two strings, it aims to find the longest common substring using hashing and binary search in order to achieve a complexity of close to linear time.
- The binary search in this program is based on the idea that if two strings have a common substring of length k, their longest common substring might be larger or equal to that but if they don't, then their largest substring will be smaller for sure.

    ```python
    while low <= high: #here high is the length of the smaller string
          mid = (low+high)//2
          result = search_hash(s1, s2, mid)
          if result['found']:
              low = mid + 1
              start1, start2, max_len = result['1'], result['2'], result['max_length']
          else:
              high = mid - 1
    ```

- Here, mid serves as that k and if a substring of length mid is found, you try a higher mid, else you move lower until you find one that works!
- To search for the hashes, it processes the 2 strings and searches for common substrings of length mid. It does so by choosing the smaller string and converting that into a hash-dictionary, where the key is a hash and the value is the index where that hash starts. For the larger one, it converts it into a regular hash-table in the form of an array where the index of the array refers to the starting position.
- It then runs through the values of the hash-table and looks for matches in the hash-dict and if found, it stores the necessary starting positions. This process repeats twice for each of the prime numbers and if both return true, this indicates that there is a definitely a common substring and the binary search moves accordingly.
