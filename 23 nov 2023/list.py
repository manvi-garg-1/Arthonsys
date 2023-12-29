'''1. Advanced Data Structures:
   - In-depth exploration of lists, sets, and dictionaries.
   - Advanced operations and methods on these data structures.
   - Use cases and practical applications for each data structure.'''




list1 =['Manvi', 'garg', 19, 20]
list1.append(22)
print(list1)


list1 = ['Manvi', 'Garg', 199, 200]
# Insert at index 2 value 10087
list1.insert(2, 100)
print(list1)

list1=[4,5,6]
list2=[9,8,7,6]
list1.extend(list2)
print(list1)
list2.extend(list1)
print(list2)

list1 = [9,8, 3, 4, 5]
print(sum(list1))

list1 =[1,4,3,5,7,1,9,3,1]
print(list1.count(1))

list1=[1,5,8,2,8,6,6,7,9,1,1]
print(len(list1))

list1 =[9,3,56,2,3,23,12,34,56]
print(list1.index(2))

num1= [7, 9, 21, 2, 22]
print(min(num1))

num1= [50, 29, 18, 10, 12]
print(max(num1))

list1= [3, 4.5, 3.9, 5.3, 1.0, 9.5]
list1.sort(reverse=True)
print(list1)

list1 = [9.5,4,6,3.5,2.7,1]
print(list1.pop())

list1 = [22, 4.5, 30, 5.3, 10.2, 9.5]
del list1[1]
print(list1)

list1 = [23, 9.4, 32, 1, 4.3, 3, 1.0, 2.5]
list1.remove(3)
print(list1)