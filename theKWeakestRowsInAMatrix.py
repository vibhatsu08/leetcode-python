# The K Weakest Rows in a Matrix
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

def kWeakestRows (mat, k) :
    matRowSums = {}
    i = 0
    for row in mat :
        matRowSums[i] = sum(row)
        i += 1
    sortedMatRowSum = dict(sorted(matRowSums.items(), key = lambda x:x[1]))
    answer = []
    for i, value in enumerate (sortedMatRowSum) :
        answer.append(value)
    return answer[:k]
print(kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2))