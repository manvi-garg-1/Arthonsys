#13. Split a string into words and count the frequency of each word.

str1='hello my name is manvi manvi and i am going to delhi'
list1=str1.split()
print(list1)
dict1=dict()
for word in list1:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1
print(dict1)