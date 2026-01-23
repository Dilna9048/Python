units = int(input("Enter water usage in liters: "))

if units <= 1000:
    bill = units * 2
elif units <= 5000:
    bill = (1000 * 2) + (units - 1000) * 3
elif units <= 10000:
    bill = (1000 * 2) + (4000 * 3) + (units - 5000) * 5
else:
    bill = (1000 * 2) + (4000 * 3) + (5000 * 5) + (units - 10000) * 10

print("Total Water Bill: ₹", bill)
