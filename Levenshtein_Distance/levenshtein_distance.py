import numpy as np


def find_levenshtein(str1, str2):
    size_x = len(str1) + 1
    size_y = len(str2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y
    for x in range(1, size_x):
        for y in range(1, size_y):
            if str1[x-1] == str2[y-1]:
                matrix[x, y] = matrix[x-1, y-1]
            else:
                matrix[x, y] = min(matrix[x-1, y-1]+1, matrix[x-1, y]+1, matrix[x, y-1]+1)
    return(int(matrix[size_x - 1, size_y - 1]))


print(find_levenshtein('hackerrank', 'leetcode'))
