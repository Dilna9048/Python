amount = float(input("Enter purchase amount: "))

if amount > 5000:
    discount = amount * 0.20
    total = amount - discount
    print("Discount:", discount)
    print("Amount to pay:", total)

elif amount > 2000:
    discount = amount * 0.10
    total = amount - discount
    print("Discount:", discount)
    print("Amount to pay:", total)

else:
    print("No discount")
    print("Amount to pay:", amount)
