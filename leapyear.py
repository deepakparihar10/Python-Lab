y=eval(input('Enter the year'))
if y%4==0:
    if y%100!=0:
        print('Leap Year')
    else:
        if y%400==0:
            print('Leap Year')
        else:
            print('Not Leap year')
else:
    print('Not Leap year')
