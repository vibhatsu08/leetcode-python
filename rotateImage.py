# Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate (matrix) :
    # find transpose of a matrix.
    for i in range (len(matrix)) :
        for j in range (len(matrix)) :
            if i <= j :
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # swap the elements from 0 till halfway, and from halfway till the end. 
    for i in range (len(matrix)) :
        for j in range (len(matrix)//2) :
            matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]
    return matrix
print(rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))