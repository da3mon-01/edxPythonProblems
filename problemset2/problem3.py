#!/usr/bin/python

balance = 999999
annualInterestRate = 0.18

monthlyInterest = annualInterestRate / 12.0
monthlyPayLow = balance / 12.0
monthlyPayHigh = (balance * (1 + monthlyInterest)**12)/12.0
monthlyPayMid = (monthlyPayLow + monthlyPayHigh) / 2.0

found = False
while found != True:
    paidoffBalance = balance
    for i in range(12):
        monthlyUnpaidBalance = paidoffBalance - monthlyPayMid
        paidoffBalance = monthlyUnpaidBalance + monthlyInterest * monthlyUnpaidBalance
    if paidoffBalance <= 0:
        if abs(paidoffBalance) > 1:
            monthlyPayHigh = monthlyPayMid
        else:
            found = True
            break      
    else:
        monthlyPayLow = monthlyPayMid

    monthlyPayMid = (monthlyPayLow + monthlyPayHigh) / 2.0


print("Lowest Payment: "+str(round(monthlyPayMid, 2)))
