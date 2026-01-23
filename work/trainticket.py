travel_class = input("Enter class (Sleeper / AC / First): ")
age = int(input("Enter age: "))

if travel_class == "Sleeper":
    fare = 300
elif travel_class == "AC":
    fare = 700
elif travel_class == "First":
    fare = 1200
else:
    print("Invalid class")
    exit()

if age < 5:
    final_fare = 0
elif age <= 12:
    final_fare = fare / 2
elif age > 60:
    final_fare = fare * 0.7
else:
    final_fare = fare

print("Final Ticket Fare: ₹", final_fare)
