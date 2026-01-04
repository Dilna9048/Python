a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b ** 2) - (4 * a * c)

if d > 0:
    print("Real and Distinct Roots")
elif d == 0:
    print("Real and Equal Roots")
else:
    print("Imaginary Roots")
