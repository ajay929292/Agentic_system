print(0 and 9)
print(0 or 3)
print(True and 0 or 5)
print(False or 0 and 10 or 5)


"""Take a number as input and check:
      positive
      negative
      zero   
"""
user_input=int(input("Enter a number : "))
if user_input == 0:
    print("Zero")
elif user_input<=0:
    print("Negative") 
else:
    print("Possitive")  

""" Take 2 numbers and print the greater one using if-else.
"""

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

if num1>num2:
    print(f"{num1} is greater then {num2}")
elif num2>num1:
    print(f"{num2} is greater then {num1}") 
else:
    print("Both number are same") 

"""ake marks as input and print grade:
90+ → A
75–89 → B
50–74 → C
<50 → Fail"""  

marks=int(input("Enter your marks : "))
if marks>=90:
    print("Grade A")
elif (marks>=75) and (marks<=89): 
    print("Grade B") 
elif (marks>=50) and (marks<=74): 
    print("Grade c")  
else:
    print("Fail") 


"""Write program to check if number is divisible by both 3 and 5."""

num=int(input("Enter a number : "))
if (num%3==0) and (num%5==0):
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by both 3 and 5")   

"""Write program to print:
     'Eligible' if age ≥18 AND salary ≥20000"""

age=int(input("Enter your age : "))
salary=int(input("Enter your salary : "))

if (age>=18) and (salary>=20000):
    print("You are Eligible")
else:
    print("You are not Eligible")    