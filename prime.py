count=0
n=eval(input('Enter the number'))
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print('Number is Prime',n)
else:
    print('Number is not Prime',n)
