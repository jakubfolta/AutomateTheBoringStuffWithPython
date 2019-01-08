grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rows = len(grid)
cols = len(grid[0])
def printTheImageFromGrid(argument):
    for x in range(cols):
        for y in range(rows):
            print(grid[y][x], end = '')
        print()
            
printTheImageFromGrid(grid)


def printPictureFromGrid(argument):
    for x in range(6):
        for y in range(9):
            print(argument[y][x], end = '')


printPictureFromGrid(grid)
        
    



































        
    
    
