# Sort the Students by Their Kth Score
# There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.
# You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.
# Return the matrix after sorting it.

def sortTheStudents (score, k) :
    # to loop through the rows
    for i in range (len(score)) :
        # to iterate through the columns
        for j in range (len(score)-i-1) :
            # to iterate through only the elements in the kth column, and sort the rows accordingly
            if score[j][k] < score[j+1][k] :
                score[j], score[j+1] = score[j+1], score[j]
    return score
print(sortTheStudents(score = [[3,4],[5,6]], k = 0))