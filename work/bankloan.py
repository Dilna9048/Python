salary = int(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))

if salary >= 50000 and credit_score >= 700:
    print("✅ Loan Approved")
elif salary >= 30000 and credit_score >= 600:
    print("⚠️ Partially Approved")
else:
    print("❌ Loan Rejected")
