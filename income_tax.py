def calculate_income_tax(income):
    """
    Function to calculate income tax based on a dynamic tax slab system.
    
    :param income: Annual income of the user.
    :return: Calculated income tax.
    """

    tax_slabs = [
        (250000, 0),          
        (500000, 0.05),      
        (1000000, 0.2),       
        (float('inf'), 0.3)  
    ]
    
    tax = 0
    previous_limit = 0

    for limit, rate in tax_slabs:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return tax


def main():
    print("Income Tax Generator")
    print("--------------------")
    
    try:
        # Input: Annual income
        annual_income = input("Enter your annual income: ₹").replace(",", "")
        
        if not annual_income.replace('.', '').isdigit():
            raise ValueError("Invalid input. Please enter a valid numeric value.")
        
        annual_income = float(annual_income)
        
        if annual_income < 0:
            print("Income cannot be negative. Please enter a valid amount.")
            return
        
        tax_amount = calculate_income_tax(annual_income)
        
        print(f"\nYour annual income: ₹{annual_income:,.2f}")
        print(f"Income tax payable: ₹{tax_amount:,.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
