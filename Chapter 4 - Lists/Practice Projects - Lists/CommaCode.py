'''Write a functon that takes a list value as an argument and returns a string with all the items separated by
a comma and a space, with "and" inserted before the last item.

The function should work with list size passed to it'''

def commacode(list_range):

    if len(list_range) > 1:
        for i in range(len(list_range)): #Get count of list items to use in for loop
            #print(i)
            #Say the list items are 4 and i = 0. Then for each iteration of the loop add that to the string variable list_a
            #_ except for when 4-3 = 1
            position = len(list_range) - i
            list_a = "" # Empty variable for all list items except the last item
            list_b = "" # Empty variable for last list item
            if position != 1:
                list_a += str(list_range[i]) + ','
                print(list_a, end = ' ') #Print all items on the same line except for last item
            else:
                list_b += 'and ' + str(list_range[i])
                
        print(list_b) #Print last item on the same line

    #If there is only one item in the list just print the one itme
    else:
        for i in range(len(list_range)):
            print(list_range[i])
            
rangeoflist = ['apples','bananas','tofu','cats']

commacode(rangeoflist)
    
