num = input("Enter a list of numbers separated by spaces: ")
num = list(map(int, num.split()))
print("The list:",num)
largest = max(num)
smallest = min(num)

print("Largest number:", largest)
print("Smallest number:", smallest)