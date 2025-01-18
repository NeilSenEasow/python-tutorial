initial_investment = int(input("Enter your initial investment: "))
final_value_investment = int(input("Enter your final value investment: "))
duration = int(input("Enter the duration of the investment: "))

roi = (final_value_investment - initial_investment) / initial_investment * 100
total_investment_growth = final_value_investment - initial_investment
compound_annual_growth_rate = float((final_value_investment / initial_investment) ** (1 / duration) - 1)
yearly_growth = float(total_investment_growth / duration)

print("Your ROI: ",roi)
print("Your total investment growth: ",total_investment_growth)
print("Your compound annual growth rate: ",compound_annual_growth_rate*100)
print("Your compound annual growth rate: %.2f" %(compound_annual_growth_rate*100))
print("Your yearly growth: %.2f" %(yearly_growth))

# print("ROI","CAGR","Yearly Growth")       
# # for k, v in d.items():
# #         print(k, end='\t')
# #         print(v.count('s1'), end='\t')
# #         print(v.count('s2'))    
# print("============================================================================================================")
