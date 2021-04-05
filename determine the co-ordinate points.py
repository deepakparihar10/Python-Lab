#Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and determine whether the point is inside the circle, on the circle or outside the circle.
x=eval(input('Enter the X co-ordinate'))
y=eval(input('Enter the Y co-ordinate'))
a=eval(input('Enter the X co-ordinate of a centre'))
b=eval(input('Enter the Y co-ordinate of a centre'))
r=eval(input('Enter the radius of a circle'))
import math
r1=math.sqrt(((x-a)**2)+((y-b)**2))
if r1==r:
    print('On the circle')
elif r1<r:
    print('Inside the circle')
else:
    print('outside the circle')
