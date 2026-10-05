print("📊 SPPU ENGG ATTENDANCE TRACKER✨ ")
print(" Maintain 75% Attendence🏆 ")

subject = input("📗Enter subject name: ")
# 1. Added int() here to convert text inputs into numbers
conducted = int(input("🖥️Total lectures conducted: "))
attended = int(input(" 📝Total lectures Attended by you: "))

if attended > conducted:
    print("🚨Hold on! Attended lectures cannot be greater than conducted lectures😅")
else:
    if conducted == 0:
        percentage = 100.0
    else:
        percentage = (attended / conducted) * 100

    print("\n📊 Attendance Report") 
    print(f"Subject: {subject}")   
    print(f"Current attendance: {percentage:.2f}%") 

    if percentage >= 75.0:
        print("🎉Status: SAFE ZONE!👍🥳")
        print("Keep it up!🏆 You are completing Sppu 75% criteria.")
    else:
        print("Status: 🚨Critical zone!😢")
        print("Your attendance is below the 75% Sppu")
