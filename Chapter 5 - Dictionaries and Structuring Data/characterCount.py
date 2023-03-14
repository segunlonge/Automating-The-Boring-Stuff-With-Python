'''A short program that counts the number of occurances of each letter in a string'''

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

#for loop; loop through each character in the 'message' sting variable

for character in message:
    #Ensure the first occurance of the character is stored in the dictionary with 0 default value
    count.setdefault(character,0)
    #increment the value of the key by 1 for each occurance
    count[character] = count[character] + 1

print(count)
