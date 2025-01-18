initial_investment = int(input("Enter your initial investment: "))
final_value_investment = int(input("Enter your final value investment: "))
duration = int(input("Enter the duration of the investment: "))

roi = (final_value_investment - initial_investment) / initial_investment * 100
total_investment_growth = final_value_investment - initial_investment
compound_annual_growth_rate = float((final_value_investment / initial_investment) ** (1 / duration) - 1)
yearly_growth = float(total_investment_growth / duration)

# print("Your ROI: ",roi)
# print("Your total investment growth: ",total_investment_growth)
# print("Your compound annual growth rate: ",compound_annual_growth_rate*100)
# print("Your compound annual growth rate: %.2f" %(compound_annual_growth_rate))
# print("Your yearly growth: %.2f" %(yearly_growth))

print("============================================================================================================")
print("ROI |","CAGR  |"," Yearly_Growth")       
print("============================================================================================================")
print("%d  | %.2f | %.2f" %(roi, compound_annual_growth_rate*100, yearly_growth))
print("============================================================================================================")

# Example inputs
# initial_investment = 10000
# final_value_investment = 15000
# duration = 3

# Output:
# ROI   | CAGR  | Yearly_Growth
# 50.00 | 14.47 | 1666.67



