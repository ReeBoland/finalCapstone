import math

#Explanations that the user will see
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan")

portfolio = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#If the client selects investment or bond

if portfolio == 'investment':
    amount = int(input("How much money are you depositing? "))
    rate = float(input("Please enter the interest rate: "))
    years = int(input("How many years do you plan on investing? "))
    interest = input("Would you like compound or simple interest? ").lower()
    r = (rate / 100)
    compound = amount + math.pow((1+r),years) 
    simple = amount*(1 + r * years)
    if interest == 'compound':    
        print(compound)
    elif interest == 'simple':
        print(simple)
elif portfolio == 'bond':
    value = float(input("Please enter the value of the house: "))
    bond_rate = float(input("Please enter the interest rate: "))
    months = int(input("How many months will you take to repay the bond? "))
    monthly_rate = ((bond_rate / 100) / 12)
    repayment = (monthly_rate * value) / (1 - (1 + monthly_rate)**(months))
    print(abs(repayment)) 
else:
    print("Please enter a valid command.")