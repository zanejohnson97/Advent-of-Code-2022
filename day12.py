# BFS search algorithm
from collections import deque as queue

# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]
 
# Function to check if a cell
# is to be visited or not
def isValid(vis, row, col, numRows, numCols, grid, elevation):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= numRows or col >= numCols):
        return False
 
    # If cell is already visited
    if (vis[row][col]):
        return False

    if grid[row][col] - elevation >= 2:
        return False

    # Otherwise
    return True

# Function to perform the BFS traversal
def BFS(grid, vis, row, col, end):
   
    # Stores indices of the matrix cells
    q = queue()
 
    # Mark the starting cell as visited
    # and push it into the queue
    q.append(( row, col ))
    vis[row][col] = True

    # find number of rows and number of columns
    numRows = len(grid)
    numCols = len(grid[0])

    # step counter
    step=0
    layer1 = 2
    layer2 = 0
    # Iterate while the queue
    # is not empty or not at end
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        elevation = grid[x][y]

        layer1 = layer1-1
        if layer1 == 0:
            step = step+1
            layer1 = layer2
            layer2 = 0
        
        # check for end
        if [x,y] == end:
            return step

        # print(grid[x][y], end = " ")
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy, numRows, numCols, grid, elevation)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
                layer2 = layer2+1

f = open('day12.txt')
lines = f.readlines()
lines = [x.strip('\n') for x in lines]

grid = []
As = []
for i in range(len(lines)):
    tempGrid = list(lines[i])
    for j in range(len(tempGrid)):
        if tempGrid[j] == 'a':
            As.append([i,j])
        if tempGrid[j] == 'S':   
            tempGrid[j] = 97
        elif tempGrid[j] == 'E':
            tempGrid[j] = 122
            end = [i,j]
        else:
            tempGrid[j] = ord(tempGrid[j])
    grid.append(tempGrid)

steps = []
for A in As:
    vis = [[ False for i in range(len(grid[0]))] for j in range(len(grid))]
    steps.append(BFS(grid, vis, A[0], A[1], end))   

res = []
for val in steps:
    if val != None :
        res.append(val)

print(min(res))     