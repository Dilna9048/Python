marks = []

for i in range(1, 6):
    m = float(input(f"Enter subject {i} marks: "))
    marks.append(m)

average = sum(marks) / 5
print("Average:", average)

if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 50:
    print("Grade C")
elif average >= 35:
    print("Pass with Grace")
else:
    print("Fail")
