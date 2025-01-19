input_string = input("Enter a string: ")
key = int(input("Enter a key: "))
encrypted_string = ""

for ch in input_string:
    encrypted_string += chr(ord(ch) + key)

print("The encrypted string is: ", encrypted_string)
