num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))

print("Choices Available are ")
print("1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")

choice = int(input("Enter Choice: "))

print("Your Choices are")

if choice == 1:
    print(f"Result = {num1 + num2}")
elif choice == 2:
    print(f"Result = {num1 - num2}")
elif choice == 3:
    print(f"Result = {num1 / num2}")
elif choice == 4:
    print(f"Result = {num1 * num2}")
else:
    print("Invalid Operation")