n=eval(input('Enter the number of lines'))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i+'*'*(i-1))
