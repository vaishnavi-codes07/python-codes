#Hostel Water Tracker

print("💦💧=====Hostel Water Tracker====")
print("Track your water intake & beat the pune heat!🥵")

base_target=2.5

print("What describes your activity level today?")
print("1. Sitting in hostel room studying")
print("2. Walked to campus labs")

activity=input("select choice(1/2) :")

if activity=="2":
  total_target=base_target+1.0
  print("Activity Detected: Target increased to 3.5 liters🎯")
else:
  total_target=base_target
  print("Studying today: target set to 2.5 liters📗")

water_drank=float(input("How many liters of water 🌊 you drank today?"))

remaining_water=total_target-water_drank

if remaining_water<=0:
  print("🟢Status: perfectly hydrated")
else:
  print("🔴Dehydration risk")

if remaining_water>1.5:
  print("Action required: Drink water💦")
else:
  print("Drink 1-2 glass more")
