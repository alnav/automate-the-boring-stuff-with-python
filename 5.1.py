"""
5.1 Fantasy Game

You are creating a fantasy video game. 
The data structure to model the player’s inventory will be a dictionary where the keys are string values describing 
the item in the inventory and the value is an integer value detailing how many of that item the player has. 
For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
means the player has 1 rope, 6 torches, 42 gold coins, and so on.
Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    """
    Dictionary -> Null
    Print formatted items in inventory
    """

    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

"""
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

The previous program (with your displayInventory() function from the previous project) would output the following:


Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
"""

def addToInventory(inventory, addedItems):
    """
    Dictionary List -> Null
    Add addedItems to inventory
    """
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)
