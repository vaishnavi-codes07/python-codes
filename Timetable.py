print(f"-------SPPU 1st year Timetable bot-------")

day=input("Enter current day:")
current_time=input("Enter current time:")

print(day)
print(current_time)

if day=="Monday":
  if current_time=="8:30":
    print("Alert: Engineering Mathemetics lecture starts at 9:00 (Room no. 410)")
  elif current_time=="11:00":
    print("Alert Basic Electronics lab at 11:30 (Lab 3)")
  else:
    print("You have no lecture at this time!")

elif day=="Tuesday":
  if current_time=="9:00":
    print("Alert: Engineering physics lecture starts at 9:30 (Room no 408)")
  elif current_time=="11:00":
    print("Alert: Programming lab at 12:00 (Lab 5)")
  else:
    print("You have no lecture at this time!")

elif day=="Wednesday":
  if current_time=="9:00":
    print("Alert: Basic Electronics Lecture at 9:15 (Room no 405)")
  elif current_time=="10:30":
    print("Alert: Communication skills lecture at 11:00 (Room no 403)")
  else:
    print("You have no lecture at this time!")

elif day=="Thursday":
  if current_time=="8:30":
    print("Alert: Programming language lecture at 9:00 (Room no 410)")
  elif current_time=="10:30":
    print("Alert: Engineering Mathematics lecture at 11:00 (Room no 410)")
  else:
    print("You have no lecture at this time!")

elif day=="Friday":
  if current_time=="8:30":
    print("Alert: Mechanics lecture at 9:00 (Room no 408)")
  else:
    print("You have no lecture at this time!")


else:
 print("Weekend vibes!... Time to upgrade your skills or just chill!")

print("---------Thank you---------")
