# Delete Greatest Value in Each Row
# You are given an m x n matrix grid consisting of positive integers.
# Perform the following operation until grid becomes empty:
# Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.
# Return the answer after performing the operations described above.

def deleteGreatestValue (grid) :
    sum = 0
    maxValues = 0
    for i in range (len(grid)) :
        grid[i].sort()
    for i in range (len(grid[0])) :
        for j in range (len(grid)) :
            maxValues = max(grid[j][i], maxValues)
        sum += maxValues
    return sum
print(deleteGreatestValue(grid=[[9,81],[33,17]]))