### Part One -- your code goes here. 

for i in range(1, 11):   # iterates a variable (in this case i) in the range 0-10 ((1, 11) because python counts from 0)
  squareNumber = i **2    # makes the variable i equal 'squareNumber' and is squared until the end of the range
  print(squareNumber)      # prints the variable 'squareNumber'
  if i == 10:               # for added measure the iteration is stopped when i == 10
    break                    # breaks out the loop once the if statement condition is met or the range is finished