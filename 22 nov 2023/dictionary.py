#15. Create a dictionary from two lists (keys and values).

test_keys = ["manvi", "deeksha", "preeti"]
test_values = [1, 2, 3]
# Printing original keys-value lists
print("Original key list is : " ,(test_keys))
print("Original value list is : " , (test_values))
# using dictionary comprehension
# to convert lists to dictionary
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
print("Resultant dictionary is : " + str(res))