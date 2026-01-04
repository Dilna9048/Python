amount = float(input("Input the amount of purchase: "))

if amount > 1000:
    discount = amount * 0.10
    total = amount - discount
    print("Discount:", discount)
    print("Amount to pay:", total)
else:
    print("No discount")
    print("Amount to pay:", amount)
