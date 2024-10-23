### Part Four -- your code goes here. 
import random
x = 0                                     # makes the variable x equal zero
randList = []                              # makes the variable 'randList' a blank list
for i in range(0, 10):                      # the for loop iterates the blank list of 10 numbers (the range)
 randList.append(random.randint(0, 100))     # the append() function is used to add the numbers randomly selected within 0 and 100
while x < len(randList):                      # the while statement is used to iterate the individual integer checks in the list 'randList'
 if randList[x] % 2 == 0:                 # the if statement checks if the integer of remainder of x equals zero
   randList.pop(x)                         # if the if statement is true then the number in the list is deleted 
 else:                                    
  x = x + 1                                  # whether the statment was true or false, x is incremented by 1 to continue the while loop
print(randList)                               # prints the final list of 'randList'