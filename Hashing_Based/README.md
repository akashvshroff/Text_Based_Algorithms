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
- To illustrate this, consider a simple hashing algorithm where keys are converted to their ASCII value, summed and the sum is then taken mod 20 (If you are unfamiliar with modular arithmetic or do not remember it, please take a refresher [here]([https://brilliant.org/wiki/modular-arithmetic/](https://brilliant.org/wiki/modular-arithmetic/)) since I refer to it a lot!)
- The string "ABC" would therefore be (65+66+67)%20 which is 198%20 which is finally 18. While the string "ABCDBSDBBEHWBEWHEB" would be 12 (take my word for it...). Using such a procedure, any string can be converted to a number from 0 to 19. A side note: if we have we want to store only strings as keys, we have successfully implemented a basic version of a dictionary! We can maintain an array of size 20 and therefore for any key, you can convert it to an index position and store a value at the corresponding position! Any conversion therefore cannot be random since you want to be able to access the same index!
- Now there are glaring issues with our implementation but one such error stands out - look at the string "ABC" and the string "UVW". Using this procedure, we get the same hash value - 18. This is called a **collision**.

### What is a collision?
- A collision is a situation where 2 keys that are not equal, have the same hash and this can lead to some problems but can be well avoided by choosing a better hash function (Here I thought my simple hash function was enough...)
- Above I discussed using hashing to implement a dictionary but a dictionary has to be built to account for collisions - this can be done by storing a tuple of (key, value) in a list at the index position instead of storing just the value. Therefore in case of a collision, the tuple can simply be appended to the end of the list at the index position and to find a key, you can scan the list at the index position and match the key. Thus, it is very important to ensure that you get a dictionary with relatively fast look-ups, you have you craft a hash-function that can evenly distribute hashes across the indices and doesn't simply hash everything to the same value.

### What is a good hash?
