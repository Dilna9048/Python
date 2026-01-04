n = input("Enter number: ")
count = 0

for d in n:
    if int(d) % 2 != 0:
        count += 1

print(count)
