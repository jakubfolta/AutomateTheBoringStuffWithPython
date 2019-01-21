stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory: ')
    totalItems = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems = totalItems + v
    print('Total number of items: ' + str(totalItems))

displayInventory(stuff)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for x in addedItems


