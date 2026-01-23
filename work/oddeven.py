num = int(input("Enter a number: "))

if num % 2 == 0 and num > 50:
    print("Number is Even and greater than 50")
elif num % 2 == 0:
    print("Number is Even but not greater than 50")
elif num > 50:
    print("Number is Odd and greater than 50")
else:
    print("Number is Odd and not greater than 50")
