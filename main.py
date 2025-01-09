def calculate_income_tax(income):
    """
    Function to calculate income tax based on a dynamic tax slab system.
    
    :param income: Annual income of the user.
    :return: Calculated income tax.
    """
    # Define tax slabs as (limit, rate)
    tax_slabs = [
        (250000, 0),          # Up to ₹2,50,000: No tax
        (500000, 0.05),       # ₹2,50,001 to ₹5,00,000: 5%
        (1000000, 0.2),       # ₹5,00,001 to ₹10,00,000: 20%
        (float('inf'), 0.3)   # Above ₹10,00,000: 30%
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
        
        # Validate and convert income
        if not annual_income.replace('.', '').isdigit():
            raise ValueError("Invalid input. Please enter a valid numeric value.")
        
        annual_income = float(annual_income)
        
        if annual_income < 0:
            print("Income cannot be negative. Please enter a valid amount.")
            return
        
        # Calculate tax
        tax_amount = calculate_income_tax(annual_income)
        
        # Output: Tax details
        print(f"\nYour annual income: ₹{annual_income:,.2f}")
        print(f"Income tax payable: ₹{tax_amount:,.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
