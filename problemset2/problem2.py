#!/usr/bin/python

balance = 3926
annualInterestRate = 0.2

def calculateMonthlyPayment(balance, monthlyInterest, monthlyPaymentRate):
    newbalance = balance
    for i in range(12):
       monthlyUnpaidBalance = newbalance - monthlyPaymentRate
       newbalance = monthlyUnpaidBalance + monthlyInterest * monthlyUnpaidBalance

    if newbalance <= 0: 
       print('Lowest payment: '+str(monthlyPaymentRate))
    else:
       monthlyPaymentRate = monthlyPaymentRate + 10
       calculateMonthlyPayment(balance, monthlyInterest, monthlyPaymentRate)

monthlyPaymentRate = 10
monthlyInterest = annualInterestRate / 12.0
calculateMonthlyPayment(balance, monthlyInterest, monthlyPaymentRate)
