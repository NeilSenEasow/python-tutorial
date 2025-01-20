income = int(input("Enter your income: "))
tax_amount = 0

if income <= 300000:
    tax_amount = 0
elif income > 300000 and income <= 600000:
    tax_amount = income * 0.05
elif income > 600000 and income <= 900000:
    tax_amount = income * 0.10
elif income > 900000 and income <= 1200000:
    tax_amount = income * 0.15
elif income > 1200000 and income <= 1500000:
    tax_amount = income * 0.20
else:
    tax_amount = income * 0.30

print(f"Your tax is {tax_amount}")