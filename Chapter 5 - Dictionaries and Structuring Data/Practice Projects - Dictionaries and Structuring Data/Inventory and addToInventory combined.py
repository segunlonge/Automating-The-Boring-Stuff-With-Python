'''

addToInventory.py and Inventory.py combined

'''

inv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    lenofdragonLoot = len(addedItems)
    for j in range(lenofdragonLoot):
        if addedItems[j] not in inventory:
            inventory.setdefault(addedItems[j],addedItems.count(addedItems[j]))
        else:
            inventory[addedItems[j]] = inventory.setdefault(addedItems[j],addedItems.count(addedItems[j]))+1
    return inventory #return the output value of the function

inv = addToInventory(inv,dragonLoot)
#print(inv)

def displayInventory(inventory2):
    print("Inventory:")
    item_total = 0
    for k, v in inventory2.items():
        print(v, end = "  ")
        print(k)
        #print(v)
        item_total += v #+= Addition Assignment
    print("")
    print("Total number of items: " + str(item_total))

displayInventory(inv)
