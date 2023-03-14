'''This is a two level nested dictionary
The is the dictionary of name and food brought
Then there's the dictionary of the fruits and the amounts as
a dictionary within the initial dictionary'''

allGuests = {'Alice':{'apples':5,'pretzels':12},
             'Bob':{'ham sandwiches':3, 'apples':2},
             'Carol':{'cups':3,'apple pies':1}}

#k is for looping through the guest names
#v is for looping through each of the food items passed as an argument to the function
def totalBrought(guests, item):
                 numBrought = 0
                 for k, v in guests.items():
                     numBrought = numBrought + v.get(item,0)
                 return numBrought

print('Number of things being bought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
    
