age = int(input("Enter age: "))
nationality = input("Enter nationality: ")

if age >= 18:
    if nationality.lower() == "indian":
        print("✅ Eligible to vote")
    else:
        print("❌ Foreign nationals can’t vote")
else:
    print("❌ Not eligible due to age")
