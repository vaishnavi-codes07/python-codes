#Positional Argument

def fullName(firstName, lastName):
  print(firstName + " " + lastName)

  fullName("Sachin", "Tendulkar")
  fullName("Virat", "Kolhi")
  fullName("Rohit", "Sharma")


#Keyword Argument

def fullName(firstName, lastName): 
  print(firstName + " "+lastName)

  fullName(lastName="Tendulkar", firstName="Sachin")


#default Argument

def fullName(firstName, lastName="Dhonnar"):
  print(firstName +" "+ lastName)

  fullName("Parshuram")
  fullName("Sunita")
  fullName("Vaishnavi")
  fullName("Vinayak")


#Variable Length Argument

def numbers(*num):
  print(num)
  print(type(num))
  print(sum(num))

  numbers(1,2,3,4,5,6,7,8,9,10)
