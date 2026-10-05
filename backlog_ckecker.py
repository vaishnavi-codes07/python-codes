print("📗✨------SPPU ATKT Check------")
year=input("year just completed[FE/SE/TE]:")

FE=int(input("fe backlogs:"))
SE=int(input("se backlogs:"))
TE=int(input("te backlogs:"))

if year=="FE":
 eligible=(FE<=4)
 print("⭐STATUS:Eligible for promotion(ATKT)")
elif year=="SE":
 eligible=(FE==0 & SE<=4)
 print("Status: Eligible for promotion")
elif year=="TE":
 eligible=(SE==0 & TE<=4)
 print("⭐STATUS:Eligible for promotion(ATKT)")
else:
 print("🚨STATUS:year down")
