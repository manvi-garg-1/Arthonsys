#6.Remove duplicates from a list while preserving the order of elements

list1 = [1, 5, 3, 6, 3, 5, 6, 1, 7]
print("The original list is : ",(list1))
# using set() to remove duplicated from list
list1 = list(set(list1))
# printing list after removal
print("The list after removing duplicates : ",(list1))


