##Program to find the hypotenuse of a right angled triangle, when the base and height are entered by the user.
h=eval(input('Enter the height'))
b=eval(input('Enter the base'))
import math
hyp=math.sqrt(b**2+h**2)
print('Hypotenuse of a right angle triangle is',hyp)
