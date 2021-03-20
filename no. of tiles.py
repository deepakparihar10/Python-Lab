##Program that calculates the number of rectangular tiles required to cover a rectangular floor if the dimensions of the floor and the dimensions of a tile are entered by the user.
lf=eval(input('Enter the length of floor'))
bf=eval(input('Enter the breadth of floor'))
lt=eval(input('Enter the length of tile'))
bt=eval(input('Enter the breadth of tile'))
areaf=lf*bf
areat=lt*bt
n=areaf//areat
print(n)
