# ====Cloud kitchen code===

print("----Online Cloud kitchen -----")
print("---------------")

print("1. 🌯Shawarma Roll -₹120")
print("2. 🍔Cheese Burger -₹90")
print("3. 🥘Special Biryani -₹180")

choice=input("Enter item number(1/2/3):")
quantity=int(input("How many units do you want?:"))

if choice=="1":
  item_name="Shawarma Roll"
  price=120

elif choice=="2":
  item_name="Cheese Burger"
  price=90

elif choice=="3":
  item_name="Special Biryani"
  price=180

else:
  item_name="Invalid Item"
  price=0

total_bill=(price*quantity)

print("----🍳🥪Order Receipt---")

if price>0:
  print(f"🍛food item:{item_name}")
  print(f"Quantity:{quantity}")
  print(f"Total Bill:₹{total_bill}")
  
  print("🛵Heading towards your Hostel gate now")

else:
  print("Invalid Choice")

print("--------------------")

