stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    totalItems = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print('Total number of items:' + str(totalItems))

displayInventory(stuff)
    
def addToInventory(inventory, addedItems):
    for x in addedItems:
        inventory.setdefault(x, 0)
        inventory[x] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print()
print('Actual inventory: ', inv)
print()
inv = addToInventory(inv, dragonLoot)
print('Found in dragon\'s den...: ', dragonLoot)
print()
print('Updated inventory: ', inv)
print()
displayInventory(inv)
