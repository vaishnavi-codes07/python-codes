import random
question=input("Ask the Magic 8-Ball a yes/no question:")
answers=[
  "Yes, definately!",
  "It is certain.",
  "Ask again later.",
  "Concentrate and ask again."
  "Don't count on it."
  "My sources say no."
]
fortune=random.choice(answers)
print(f"/ Question:{question}")
print(f"Magic 8-Ball says:{fortune}")
