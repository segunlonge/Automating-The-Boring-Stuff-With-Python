'''Write a function named collatz () that has one parameter named number. If number is even, then collatz()
should print number //2 and return this value. If number is odd, then collatz() should print and return 3*number + 1'''

def collatz(number): #The value passed to the function (argument)_
    # is stored in the parameter variable called number
    if number%2 == 0:
        return number//2 #return the value of whatever the argument _
    #that was passed to the function via the parameter if even number i.e. no remainder
    else:
        return 3*number+1 #return the value of whatever the _
    #argument that was passed to the function via the parameter if odd number

#Use the try/except method to capture exception error due to non-integer input
try:
    numberinput = int(input("Please enter an integer: ")) #Accept input from user with prompt; convert input to integer
except ValueError:
    print('Error: Must enter a integer')

#Use the try/except method to capture exception error due to no value function input
try:          
    ans1 = 0
    while ans1 != 1: # While the output of the function is not equal to 1 repeat the function _
        # until it is equal to 1
        ans1 = collatz(numberinput)
        numberinput = ans1
        print(ans1)
except NameError:
    print('Error: Unable to generate output without valid input')


        
