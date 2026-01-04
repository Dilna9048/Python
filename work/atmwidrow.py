correct_pin = "1234"

pin = input("Enter PIN: ")
balance = float(input("Enter balance: "))
withdraw_amount = float(input("Enter withdraw amount: "))

if pin == correct_pin:
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print("✅ Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("❌ Insufficient balance")
else:
    print("❌ Invalid PIN")
