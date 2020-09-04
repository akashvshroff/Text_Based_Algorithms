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
