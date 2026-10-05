print("🎇🪔-----Hosteller's Diwali Budget manager----🎆")

budget=int(input("Enter your total Diwali budget"))

print("🧨Enter your estimated expenses")

travel_cost=int(input("Travel:"))
gift_cost=int(input("gifts for family:"))
sweet_cost=int(input("Sweets & Crackers:"))
food_cost=int(input("outings & cafe treats"))

Total_expense=travel_cost+gift_cost+sweet_cost+food_cost
remaining_balance=budget-Total_expense

print(f"Total Budget:{budget}")
print(f"Total Expenses:{Total_expense}")

if remaining_balance>=0:
  print(f"Safe zone! you have {remaining_balance} left")

else:
  print("Budget crash!")
