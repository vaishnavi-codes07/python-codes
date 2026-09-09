scores=[99,90,92,88,80]
results=[]
for s in scores:
  if s>=91:
    results.append("Pass")
  else:
    results.append("Fail")
print(results)
