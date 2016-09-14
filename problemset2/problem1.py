#!/usr/bin/python

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def calculcateRemainingBalance(balance, monthlyInterest, monthsRemaining):
    '''
    This function calculates the remaning balance after a year.

    '''

    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    newbalance = monthlyUnpaidBalance + monthlyInterest * monthlyUnpaidBalance
    #print("Remaining Balance: "+ str(round(newbalance, 2)))
    monthsRemaining = monthsRemaining - 1
    if monthsRemaining > 0 :
        calculcateRemainingBalance(newbalance, monthlyInterest, monthsRemaining)
    else:
       print('Remaining Balance: '+str(round(newbalance, 2)))


monthsRemaining = 12
monthlyInterest = annualInterestRate / 12.0
calculcateRemainingBalance(balance, monthlyInterest, monthsRemaining)
