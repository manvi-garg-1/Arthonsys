#18. Rotate elements in a list by a specified number of positions.

list1=[22,34,67,35,13]
print('primary list:',list1)
list1=list1[3:]+list1[:3]
print('output of the list after left rotate by 3:',list1)
list1=list1[-3:]+list1[:-3]
print('output of the list after right rotate by 3(back to primary list):',list1)
list1=list1[-2:]+list1[:-2]
print('output of the list after right rotate by 2:',list1)
list1=list1[1:]+list1[:1]
print('output of the list after left rotate by 1:',list1)