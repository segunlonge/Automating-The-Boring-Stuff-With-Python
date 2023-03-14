tableData = [['apples','oranges','cherries','banana'],
	     ['Alice','Bob','Carol','David'],
	     ['dogs','cats','moose','goose']
             ]

def printTable(tData):

    StringSizeStore = [] #declare an empty list to store max length of string in each inner list
    StringValueStore = []
    
    for i in range(len(tData)):
        #StringSizeStore = [i]*len(tData[i])
        #Append each count of inner list in tableData by the total count of outlist
        StringSizeStore.append([i]*len(tData[i]))

    for i in range(len(tData)+1):
        #StringSizeStore = [i]*len(tData[i])
        #Append each count of inner list in tableData by the total count of outlist
        StringValueStore.append([i]*len(tData))
    
                   
    #Get the len of each inner list value
    for j in range(len(tData)):
        for k in range(len(tData[j])):
            #print(len(tData[j][k]))
            StringSizeStore[j][k] = len(tData[j][k])
    #print(StringSizeStore)

    col_lengths = []
    for j in range(len(StringSizeStore)):
        col_lengths.append(max((StringSizeStore[j])))
##    print(col_lengths)
##    print(max(col_lengths))

    right_justified_length = max(col_lengths)

##    print(StringSizeStore)
##    print(StringValueStore)
    
    for i in range(len(tData)):
        for j in range(0,len(tData[i])):
##                       print(tData[i][j])
##                       print(i,j)
##                       print(j,i)

                       # Transpose the tableData items to StringValueStore
                       StringValueStore[j][i] = tData[i][j]

# Neat trick to print each item in the k loop on a different line
    for k in range(0,len(tData[i])):
        for l in range(0,len(tData)):
            print(StringValueStore[k][l].rjust(right_justified_length)," ", end = '') #Use end = '' to print each item in the sub list on the same line
        print("")
                               
printTable(tableData)
