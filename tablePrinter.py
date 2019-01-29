tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLongestString(table):
    colWidth = [0] * len(table)
    cols = len(table[0])
    rows = len(table)
    
    for x in range(rows):
        for y in range(cols):
            if colWidth[x] < len(table[x][y]):
                    colWidth[x] = len(table[x][y])
    return colWidth
            
            
def printTableJustifiedToLongestStringInRow(table):
    cols = len(tableData[0])
    rows = len(tableData)
    colWidths = findLongestString(tableData)

    for x in range(cols):
        for y in range(rows):
            print((table[y][x]).rjust(colWidths[y]), end = ' ')
        print()
    
printTableJustifiedToLongestStringInRow(tableData)
