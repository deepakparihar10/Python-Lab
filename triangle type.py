##Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of the triangle are entered by the user.
a=eval(input('Enter the 1st side of a triangle'))
b=eval(input('Enter the 2nd side of a triangle'))
c=eval(input('Enter the 3rd side of a triangle'))
if a+b>c or b+c>a or a+c>b:
    if a==b or a==c or b==c:
        print('Isoscele Triangle')
    elif a!=b or a!=c or b!=c:
        print('Scalene Triangle')
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print('Right angle Triangle')
else:
    print('Invalid Triangle')
