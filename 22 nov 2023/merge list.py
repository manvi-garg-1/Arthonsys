#17. Merge two sorted lists into a single sorted list.

list1 = [10, 54, 61, 9, 11]
list2 = [3, 46, 7, 20, 30]
# printing original lists
print("The original list 1 is : " ,(list1))
print("The original list 2 is : " ,(list2))
# using sorted()
# to combine two sorted lists
res = sorted(list1 + list2)
print("The combined sorted list is : " ,(res))