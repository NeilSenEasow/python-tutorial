numbers= []
while True:
    num = input("Enter a number (or type 'done' to stop): ")
    if num == 'done':
        break
    numbers.append(int(num))

print("List of numbers:", numbers)
new_list=[num for num in numbers if num % 2 == 0 ]

new_list.sort()
print("List of even numbers in ascending order:", new_list)
  