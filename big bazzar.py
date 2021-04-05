#Big Bazaar specifies its customers into three categories as Bronze, Silver and Gold. If the shopping amount is greater than 25000, the category is GOLD. If the shopping amount is between 10000 and 25000, the category is SILVER, otherwise the category is BRONZE. The discount offered for GOLD customers is 20% of the shopping amount, for SILVER customers is 10% of the shopping amount and 5% otherwise. Design a program in python that asks the user to input the total shopping amount, outputs the category and amount to be paid.
ta=eval(input('Enter the total amount'))
if ta>25000:
    print('GOLD')
    a=(ta*20)/100
    am=ta-a
    print('Amount to be paid',am)
elif ta>10000 and ta<25000:
    print('SILVER')
    b=(ta*10)/100
    amo=ta-b
    print('Amount to be paid',amo)
else:
    print('BRONZE')
    c=(ta*5)/100
    amt=ta-c
    print('Amount to be paid',amt)
