#3.Calculate the sum of elements in a list of integers.

total = 0
list1 = [11, 5, 17, 18, 23]
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list:", total)