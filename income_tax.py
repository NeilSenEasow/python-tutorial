income = int(input("Enter your income: "))
tax_amount = 0

if income <= 250000:
    tax_amount = 0
elif income <= 250000 and income >= 500000:
    tax_amount = income * 0.05
elif income <= 500000 and income >= 1000000:
    tax_amount = income * 0.10
else:
    tax_amount = income * 0.30

print(f"Your tax is {tax_amount}")