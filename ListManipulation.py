### Part Three -- your code goes here. 

list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] # makes list equal variable 'list'
list.sort()                            # sorts the list in ascending order
# [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
list = [i for i in list if i != 1]    # makes list equal new list that iterates and deletes the specfic condition '1' from the list
# [2, 3, 3, 4, 5, 5, 6, 9,]
list.extend([7, 8])                   # adds the list elements [7, 8] to the main list variable on the left side
# [2, 3, 3, 4, 5, 5, 6, 9, 7, 8]
print(list)