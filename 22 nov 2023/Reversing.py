#4.Reverse the order of elements in a list without using the reverse() method.

lst = [10, 15, 20, 25, 30, 35]
l = []  # empty list
for i in lst:
    l.insert(0, i)
print(l)