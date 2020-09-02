# python3
import random


def hash_function(s, X, mod):  # ONLY TO SHOW WHAT THE RELATION IS - NOT USED
    """
    Taking a string s, return its hash value by using a hash function where
    for a string s(s0,s1...sm-1) i.e of length m, the hash is a sum of s[j]*X(m-j-1)
    for j from 0 to m-1.
    """
    ans = 0
    m = len(s)
    for j in range(m):
        ans = (ans + ord(s[j])*pow(X, m-j-1)) % mod
    return ans


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


def process_queries(s, queries):
    X, h1, h2, m1, m2 = pre_process_string(s)
    # print(h1, h2)
    res = []
    for a, b, l in queries:
        a_m1 = hash_value(h1, m1, X, a, l)
        a_m2 = hash_value(h2, m2, X, a, l)
        b_m1 = hash_value(h1, m1, X, b, l)
        b_m2 = hash_value(h2, m2, X, b, l)
        if a_m1 == b_m1 and a_m2 == b_m2:
            res.append("Yes")
        else:
            res.append("No")
    return res


if __name__ == "__main__":
    s = input()
    n = int(input())
    qs = []
    for _ in range(n):
        qs.append(list(map(int, input().split())))
    # print(qs)
    rs = process_queries(s, qs)
    for r in rs:
        print(r)
