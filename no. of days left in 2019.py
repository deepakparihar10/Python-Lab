#Design a program in python to display the number of days left in the current year (2019), when today’s date is entered by the user in format of your choice.
d=eval(input('Enter the day'))
m=eval(input('Enter the month'))
if m==1:
    print('Number of days left',365-d)
elif m==2:
    print('Number of days left',365-31-d)
elif m==3:
    print('Number of days left',365-59-d)
elif m==4:
    print('Number of days left',365-90-d)
elif m==5:
    print('Number of days left',365-120-d)
elif m==6:
    print('Number of days left',365-151-d)
elif m==7:
    print('Number of days left',365-181-d)
elif m==8:
    print('Number of days left',365-212-d)
elif m==9:
    print('Number of days left',365-245-d)
elif m==10:
    print('Number of days left',365-273-d)
elif m==11:
    print('Number of days left',365-304-d)
else:
    print('Number of days left',365-334-d)
