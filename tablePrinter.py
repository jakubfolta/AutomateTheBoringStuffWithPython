tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLongestString(table):
    colWidth = [0] * len(table)
    cols = len(table[0])
    rows = len(table)
    print(colWidth)
    
    for x in range(rows):
        for y in range(cols):
            print(colWidth[x])
            if int(colWidth[x]) < int(len(table[x][y])):
                    colWidth[x] = len(table[x][y])
    return colWidth
            
            
def printTable(table):
    cols = len(tableData[0])
    rows = len(tableData)

    for x in range(cols):
        for y in range(rows):
            print((table[y][x]).rjust(8), end = ' ')
        print()
            
    print(colNumb)
    print(tableData)
    



printTable(tableData)'''
