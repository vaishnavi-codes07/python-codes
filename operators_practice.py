#Logical operators

num=6

print("Is the number divisible by 2 and 3=", num%2==0 and num%3==0)

a=7
b=12
print("Is a greater than 5 or b less than 10=", a>5 or b<10)

year=int(input("Enter a year:"))
print("Is the year a leap year=",year%4==0 and year%100!=0)

#Identity operators

list1=[11,22,3,4]
list2=[1,22,3,4]
print("Do list1 and list2 refer to the same object?",list1 is list2)

x=100
y=101
print("Are x and y different objects?",x is not y)

list1=[1,2,3,4,5]
print("Is 5 present in the list?",5 in list1)

str1="Hello World!"
print("Is Hello present in the string?",'Hello in str1')

print("Is 15 not present in the list?",15 not in list1)

set1={1,2,3}
set2={3.4.5}

set3=set1 & set2
print("set3=",set3)
