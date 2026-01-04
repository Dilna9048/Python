correct_pin = "1234"

entered_pin = input("Enter your PIN: ")

if entered_pin == correct_pin:
    print("✅ Transaction Allowed")
else:
    print("❌ Invalid PIN")
