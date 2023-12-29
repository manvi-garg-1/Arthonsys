# add Method
s = {'m','a','n','v','i'}
s.add('w')
print(s)

# union Method
s11={7,3,9,1}
s22={12,33,22,1}
print(s11.union(s22))

s4={11,33,22,88}
s5={2,66,71,5}
s6={71,12,6,2}
l=s4.union(s5).union(s6)
print(l)


# Update Method
l1=[87,43,56,23]
l2=[12,34,78]
print(l1+l2)

s23=set(l1)
s8=set(l2)
s23.update(s8)
print(s23)


# pop method
s1={9,4,7,1,3}
s1.pop()
print(s1)

#remove
set1={3,5,'three',2,"one"}
set1.remove("one")
set1.pop()
print("after remove=",set1)



# intersection Method
s25={8,3,1}
s26={7,3}
a=s25.intersection(s26)
print(a)

#difference
a= {"apple", "banana", "cherry"}
b= {"google", "microsoft", "apple"}
c = a.difference(b)


#disjoint
r={1,2,6,4}
p={3,6,9,5}
dis= r.isdisjoint(p)
print("disjoint element=",dis)

#  copy Method
s31={11,66,43,23}
print(s31)
s32=s31.copy()
print(s32)

# check if all element in set
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

