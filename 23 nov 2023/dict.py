dict1 = {'1': 'go', '2': 'to' , '3': 'home'}
dict1.clear()
print(dict1)


dict11 = {'Name': 'manvi', 'Age': '23', 'Country': 'India'}
print(dict11.get('Name'))
print(dict11.get('Gender'))


d11={'Name': 'manvi', 'Roll_no': 4, 'Age': 22}
print(d11.items())
print(list(d11.items())[1][1])


dict12 = {'Name': 'manvi', 'Age': '23', 'Country': 'India'}
print(list(dict12.keys()))


dict13 = {'Name': 'manvi', 'Age': '23', 'Country': 'India'}
print(list(dict13.values()))


dict13 = {'Name': 'manvi', 'Age': '23', 'Country': 'India'}
dict14 = {'Name': 'Neha', 'Age': '22'}
dict13.update(dict14)
print(dict13)


d = {'Name': 'manvi', 'Age': '23', 'Country': 'India'}
d.pop('Age')
print(d)


d1 = {'Name': 'manvi', 'Age': '23', 'Country': 'India'}
d1.popitem()
print(d1)
d1.popitem()
print(d1)