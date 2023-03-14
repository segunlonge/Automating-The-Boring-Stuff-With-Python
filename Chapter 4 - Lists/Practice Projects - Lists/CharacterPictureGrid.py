'''Character Picture Grid project

Turn grid below into:

..00.00..
.0000000.
.0000000.
..00000..
...000...
....0....

This is basically a transposition exercise

'''

grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

#The end='' parameter is a way to stop the print function from adding a new line

#Loop workings: print column "0" 9 times; column "1" 8 times etc

#print(range(len(grid[0]))) ==> outputs range(0, 6) - 6 not inclusive e.g. it is 0-5
#print(range(len(grid))) ==> outputs range(0, 9) - 9 not inclusive e.g. it is 0-7

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print('') #Print each row on a new line



