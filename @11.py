list1=[2,4,5,7,8]
for i in list1:
   for k in list1:
       if k>1:
           a=k
       if k<i:
           b=k
print('max=',a)
print('min=',b)
