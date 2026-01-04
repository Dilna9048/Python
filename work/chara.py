ch = input("Enter a character:")

if ch.isupper():
    print("uppercase letter")
elif ch.islower():
    print("lowercase letter")  
elif ch.isdigit():
    print("digit")  
else:
    print("special symbol")    