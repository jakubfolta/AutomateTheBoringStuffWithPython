stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory: ')
    totalItems = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems = totalItems + v
    print('Total number of items: ' + str(totalItems))

displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for x in addedItems:
        inventory.setdefault(x, 0)
        inventory[x] += 1
    return inventory
        

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print()
print(inv)
inv = addToInventory(inv, dragonLoot)
print('Found in dragon\'s den...')
displayInventory(inv)
        


