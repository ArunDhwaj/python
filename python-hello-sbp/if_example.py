i = 13

if i > 8 and i < 12:
    print(f"{i} is between 8 and 12")
    print("this is part of if")
else:
    print(f"{i} is not between 8 and 12")
    print("this is part of else")


x_string = input("Enter a Number")
x = int(x_string)

if x == 1:
    print(f"{x} is 1")
    print("this is part of if")
elif x == 2:
    print(f"{x} is 2")
    print("this is part of elif")
else:
    print(f"{x} is NOT 1 or 2")
    print("this is part of else")
