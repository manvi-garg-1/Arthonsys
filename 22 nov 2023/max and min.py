#11.Find the maximum and minimum values in a list of numbers.

list1=[4,6,8,2,5,1,9]
print('max=',max(list1))
print('min=',min(list1))

#using for loop
list1=[4,6,8,2,5,1,9]
for i in list1:
    for k in list1:
        if k>i:
            a=k
        if k<i:
            b=k
print('max=',a)
print('min=',b)