attendance = ["Present","Absent","Present","Present","Absent"]
p = 0
a = 0

for s in attendance:
    if s == "Present":
        p += 1
    else:
        a += 1

print("Present:", p)
print("Absent:", a)
