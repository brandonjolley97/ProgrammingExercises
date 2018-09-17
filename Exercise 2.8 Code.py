annualInterestRate = eval(input("Enter annual interest rate as a decimal: "))
numYears = eval(input("Enter the number of years: "))
loanAmount = eval(input("Enter the loan amount: "))

monthlyInterest = annualInterestRate / 1200
numMonths = numYears * 12
monthlyPayment = loanAmount * monthlyInterest / (1 - 1 / (1 + monthlyInterest ** numMonths))
totalPayment = monthlyPayment * numMonths
print("Your monthly payment is: " + str(int(monthlyPayment * 100) / 100))
print("Your total payments are: " + str(int(totalPayment * 100) / 100))