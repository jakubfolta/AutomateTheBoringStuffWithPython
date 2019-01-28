tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colNumb = [0] * len(table)

    for x in table:
        for y in x:
            print(y.ljust(5), end = ' ')
        print()
            
    print(colNumb)
    print(tableData)
    



printTable(tableData)
