a = float(input(" Enter side1:"))
b = float(input("Enter a side2:"))
c = float(input("Enter a side3:"))

if a==b==c:
    print("Equilateral Triangle")
elif a==b or b==c or a==c:
    print("isosceles Triangle")
else:
    print("scalence TrIangle")    