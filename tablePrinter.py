tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLongestString(table):
    colWidth = [0] * len(table)
    cols = len(table[0])
    rows = len(table)
    
    for x in range(cols):
        for y in range(rows):
            colWidth[rows].append()
            


def printTable(table):
    colWidth = [0] * len(table)
    cols = len(tableData[0])
    rows = len(tableData)

    for x in range(cols):
        for y in range(rows):
            print((table[y][x]).rjust(8), end = ' ')
        print()
            
    print(colNumb)
    print(tableData)
    



printTable(tableData)
