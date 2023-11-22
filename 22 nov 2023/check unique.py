#16. Check if all elements in a list are unique.

list1 = ['Manvi','deeksha','preeti']
print("The given list : ",list1)
# Compare length for unique elements
if(len(set(list1)) == len(list1)):
   print("All elements are unique.")
else:
   print("All elements are not unique.")
