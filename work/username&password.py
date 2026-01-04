username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("✅ Login successful")
elif username == "admin":
    print("❌ Incorrect password")
else:
    print("❌ Invalid user")
