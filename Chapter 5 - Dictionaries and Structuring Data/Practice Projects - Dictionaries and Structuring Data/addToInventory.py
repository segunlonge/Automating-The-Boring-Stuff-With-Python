'''I need to go through the list and add each item to the inventory dictionary'''

'''

1)the arguments passed into the functions are inv (dictionary) and dragonLoot (list)
2)a for loop is used to get the length of the list and the count in j is used to get the
the value of the list in the particular index.
3)if the particular list value is in not in the inventory dictionary then use the setdefault to add
the key into the dictionary and used the list count method to get the value pair of the key
4)else still use the setdefault value to return the value pair in the dictionary but increase it by one for
each value found in the list


'''

def addToInventory(inventory, addedItems):
    lenofdragonLoot = len(addedItems)
    for j in range(lenofdragonLoot):
        if addedItems[j] not in inventory:
            inventory.setdefault(addedItems[j],addedItems.count(addedItems[j]))
        else:
            inventory[addedItems[j]] = inventory.setdefault(addedItems[j],addedItems.count(addedItems[j]))+1
    print(inventory)

inv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
inv = addToInventory(inv,dragonLoot)


