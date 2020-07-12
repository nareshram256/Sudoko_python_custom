import numpy as np
import pandas as pd

def possible(y,x,n,grid):
    for i in range(0,9):
        if (grid[y][i]==n): #check n in row
            return False
    for i in range(0,9):
        if(grid[i][x]==n): #check n in col
            return False
    x0=(x//3)*3 # // is Floor division - division that results into whole number 
    y0=(y//3)*3 
    # selts the grid contains 9 elements(3x3)
    for i in range (0,3):
        for j in range(0,3):
            if(grid[y0+i][x0+j]==n):
                return False
    return True    

def solve(grid):
    for y in range (9):
        for x in range(9):
            if (grid[y][x]==0): # chacks for blanks
                for n in range(1,10):
                    if(possible(y,x,n,grid)):
                        grid[y][x]=n
                        #print(y,x,n)
                        solve(grid)            # now check for other solution
                        grid[y][x]=0
                return         
    print("\n solution found by Anusha is \n",np.matrix(grid))                     
    input('more? press enter')


if __name__ == '__main__':
    data=pd.read_excel("sudoko.xlsx",inplace=True)
    grid=data.values
    print('\n the problem is  \n',grid)
    #grid = [[7, 8, 0, 4, 0, 0, 1, 2, 0],[6, 0, 0, 0, 7, 5, 0, 0, 9],[0, 0, 0, 6, 0, 1, 0, 7, 8],[0, 0, 7, 0, 4, 0, 2, 6, 0],[0, 0, 1, 0, 5, 0, 9, 3, 0],[9, 0, 4, 0, 6, 0, 0, 0, 5],[0, 7, 0, 3, 0, 0, 0, 1, 2],[1, 2, 0, 0, 0, 7, 4, 0, 0],[0, 4, 9, 2, 0, 6, 0, 0, 7]]
 
    solve(grid)
    print("Completed")
    exit()
                
