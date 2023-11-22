#7.Perform basic arithmetic operations (addition, subtraction, multiplication, division) using user input

x=int(input('enter num1'))
y=int(input('enter num2'))
c=input('enter choice 1=add 2=sub 3=multi 4=div')

if c=='add':
    d=x+y
    print('add=',d)
if c=='sub':
    d=x-y
    print('sub=',d)
if c=='multi':
    d=x*y
    print('multi=',d)
if c=='div':
    d=x/y
    print('div=',d)
else:
    print('wrong choice')
