master_list = input("Enter a list of numbers separated by spaces: ")
master_list = list(map(int, master_list.split()))
print("The List:",master_list)
limit= int(input("Enter a limit number: "))
filtered_list = [num for num in master_list if num < limit]
print("Numbers less than", limit, ":", filtered_list)