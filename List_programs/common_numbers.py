list1= []
while True:
    num = input("Enter a number for first list(or type 'done' to stop): ")
    if num == 'done':
        break
    list1.append(int(num))

print("First List:", list1)
list2= []
while True:
    num = input("Enter a number for second list(or type 'done' to stop): ")
    if num == 'done':
        break
    list2.append(int(num))

print("Second List:", list2)

common_elements = [num for num in list1 if num in list2]
print("Common Elements in both lists:", common_elements)
