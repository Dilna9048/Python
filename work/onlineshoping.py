amount = float(input("Enter total purchase amount: "))

if amount > 10000:
    discount = amount * 0.25
elif amount >= 5000:
    discount = amount * 0.15
elif amount >= 2000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Payable Amount:", final_amount)
