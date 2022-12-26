# -*- coding: utf-8 -*-

#code08.py
from tkinter import *

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("대출 계산기")
        label(window, text="연이율").grid(row=1, column=1, sticky=w)
        label(window, text="대출년수").grid(row=2, column=1, sticky=w)
        label(window, text="대출금").grid(row=3, column=1, sticky=w)
        label(window, text="월상환금").grid(row=4, column=1, sticky=w)
        label(window, text="총상황금").grid(row=5, column=1, sticky=w)

        self.annuallnterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar,
              justify=RIGHT).grid(row=1, column=2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearVar,
              justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar,
              justify=RIGHT).grid(row=3, column=2)
        
        self.mounthlyPaymentVar = StringVar()
        lblMonthlyPayment = label(window, textvariable=self.mounthlyPaymentVar).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblMonthlyPayment = label(window, textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)
        
        btComputerPayment=Button(window, text="상환금계산하기", 
                                 command=self.computerPayment).grid(row=6, column=2, sticky=E)
        
        window.mainloop()
        
        def computerPayment(self):
            monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()), \
                                                    float
                            (self.annualInterestRateVar.get())/1200, \
                                                         int(self.numberOfYearsVar.get()))  
          self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
          #self.monthlyPaymentVar.set(monthlyPanyment)
    
          totalPayment = float(self.monthlyPaymentVar.get())*12*int
          (self.numberOfYearsVar.get())
          self.totalPaymentVar.set(format(totalPayment, "10.2f"))
          #self.totalPaymentVar.set(totalPanyment)
        def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
            monthlyPanyment = loanAmount * monthlyInterestRate / (1-1/(1+monthlyInterestRate)**(numberOfYears*12))
            return monthlyPanyment
        
        LoanCalculator()
