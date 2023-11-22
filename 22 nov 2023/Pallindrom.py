#1.. Check if a given string is a palindrome or not.

str1=input('enter string')
str2=str1[::-1]
if str1==str2:
    print('string is palindrome')
else:
    print('string is not palindrome')