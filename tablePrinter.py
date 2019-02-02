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

print()

def findLongestString(table):
    colWidths = [0] * len(table)
    rows = len(table)
    cols = len(table[0])

    for x in range(rows):
        for y in range(cols):
            if len(table[x][y]) > colWidths[x]:
                colWidths[x] = len(table[x][y])
    return colWidths

def printTableJustifiedToRowsLongestString(table):
    colsWidth = findLongestString(table)
    cols = len(table[0])
    rows = len(table)

    for x in range(0, cols):
        for y in range(0, rows):
            print((table[y][x]).rjust(colsWidth[y]), end = ' ')
        print()

printTableJustifiedToRowsLongestString(tableData)






































