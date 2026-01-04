units = [100,250,400,150]

for u in units:
    if u <= 200:
        bill = u * 5
    else:
        bill = u * 7
    print(bill)
