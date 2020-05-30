# Outline:

- The Levenshtein distance between 2 strings is the number of transformations it can take to get from one string to the other. The transformations allowed are one of three: insertion - i.e inserting a character into the initial string to get it closer to the target string, deletion - i.e deleting a character from the initial string and replacement - i.e replacing a character from the initial string to one from the target string. The Levenshtein distance therefore is the shortest number of transformations that are needed to convert one string to the other. A detailed description of how the algorithm functions lies below.

# Purpose:

- I have always been very intrigued in how one can compare two strings in order to get approximation matches, with the Levenshtein distance being one of the 2 predominant techniques: the other being Cosine Similarity which I shall hope to complete in the near future. This fascination has sort of stemmed with my interest in how autocomplete works and building algorithms such as the Markov Chain and this one could help act as integral components when I build my own autocomplete application.
- The build was my first major foray into dynamic programming which might not have been the best idea since this algorithm isn't what one would consider beginner friendly, but multiple YouTube explanations helped me understand this algorithm and figure out dynamic programming at a rudimentary level.

# Description:

- The first step to understanding the algorithm is to better understand the premise of it, imagine we were comparing two strings, "HORSE" and "ROS". How many conversions would it take to convert the former to the latter?
- The answer is 3. The steps are:
    - Convert "H" to "R", so we get "RORSE" (REPLACEMENT)
    - Delete the "R" at index 3, so we get "ROSE" (DELETION)
    - Delete the "E" at the end, so we get "ROS" as desired (DELETION)
- Therefore the solution becomes determining what the optimal choice is amongst replacement, deletion and insertion.
- Using an interative top-down approach we can break our problem into much smaller problems, solving those to choose our solution, observe the following table:

  ![alt text](https://github.com/akashvshroff/Text_Based_Algorithms/blob/master/Levenshtein_Distance/Explanation_Images/example_grid.jpg)
  
- For any row or column in the grid : i,j the number determines how to convert the string HORSE[:i+1] to ROS[:j+1].
- Therefore analysing the 2 strings, starting from an empty string till the whole string, there are 2 possible options:
    - If the 2 characters are the same, such as ' ' and ' ' the number of conversions required are 0.
    - If the characters are different, we must choose which conversion is the optimal one.
- Therefore for the first row and first column, the options are very simple as to get to ' ' from ' ', 'R', 'RO', 'ROS' is 0 or the number of characters as deletions. The same can be applied to the column where we must achieve ' ' from ' ', 'H'....'HORSE'.
- Choosing which option of transformation is optimal is easy and can be understood by understanding the relation of each transformation to the table above.
- If you are at index 2,2 (ONLY COUNTING THE PORTION OF THE GRID WITH NUMBERS), you are trying to determine how to get to 'HO' from 'RO' or vice versa:
    - Since the last character is the same, it has no impact on the number of transformations that are needed and therefore can be disregarded. The number of transformations required therefore is the same as that in the index 1,1 where we convert 'H' to 'R' which is 1.
- Now let us consider index 3,2 where we are changing 'HOR' to 'RO':
    - The last character is not the same and therefore we must choose our transformation:
    - Deletion of the last character refers to the same row but previous column as we are removing the last character from 'RO' to give us 'R' and checking index 3,1 reveals a transformation cost of 2.
    - Replacing the last character refers to the previous row, previous column and index 2,1 gives us a score of 2.
    - Inserting a character would ideally refer to the same row, next column but since this would mean we are going ahead in time, this is not possible and therefore we modify inserting a character into string1 to deleting that character from string2 as you would only insert a character that is present in string2 given the goal of optimality. Therefore we consider the previous row, same column i.e index 2,2 where our score is 1.
    - Now choosing the optimal number of transformations means choosing the lowest of these 3 scores and then adding 1 to account for our transformation.
    - Observe the following picture:
      
      ![alt text](https://github.com/akashvshroff/Text_Based_Algorithms/blob/master/Levenshtein_Distance/Explanation_Images/reference_grid.jpg) 
      
- Therefore using an iterative top-down approach, we can build our matrix row by row and our final answer becomes the number in the final row, final column - marked in blue above! That is our Levenshtein distance.
- While I do not believe text is the best means to understand complex algorithms, I hope I did a fairly okay job at explaining the program - the resources I used to understand this program are:
    - [BackToBack SWE](https://www.youtube.com/watch?v=MiqoA-yF-0M&t=639s)
    - [Gaurav Sen](https://www.youtube.com/watch?v=XJ6e4BQYJ24&t=637s)
