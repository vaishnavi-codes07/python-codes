print("=== FIXED HOSTEL BILL SPLITTER ===")

print("📋Hostel Bill Splitter")
print("Stop fighting & input your expenses")
print("Bill details")

bill_name = input("What did you pay for? ")
total_amount = int(input("💵Total Bill Amount: "))
num_roommates = int(input("No. of roommates sharing the bill: "))


share_per_person = total_amount / num_roommates

print("--- The Split Matrix ---")
print("Automated settlement ledger")


print(f"Total Bill: ₹{total_amount}")
print(f"Per person share: ₹{share_per_person:}")
print(f"Each roommate has to pay you: ₹{share_per_person:}")
