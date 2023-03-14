'''A function/program to print each item in any dictionary key/value pair
plus the total amount in the value part'''

items = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        #print(v)
        item_total += v #+= Addition Assignment
    print("")
    print("Total number of items: " + str(item_total))

displayInventory(items)
