import random
list=["snake","water","gun"]
chances=10
no_of_chances=0
human_point=0
computer_point=0

print("\t \t WELCOME TO SNAKE WATER GUN GAME BY AJAY")
print("\t You have 10 chance to win the game ")

while chances>no_of_chances:
 user_choice=input("Enter snake or water or gun : ")

 computer_choice=random.choice(list)


 if (user_choice==computer_choice):
       a=f"you entered {user_choice} and computer entered {computer_choice}"
       print(a)
       b=f"you has {human_point} point and computer has {computer_point} point"
       print(b)
       print("Draw")
 elif(user_choice=="snake" and computer_choice=="water"):
       human_point=human_point+1
       a=f"you entered {user_choice} and computer entered {computer_choice}"
       print(a)
       b=f"you has {human_point} point and computer has {computer_point} point"
       print(b)
 elif(user_choice=="snake" and computer_choice=="gun"):
       computer_point=computer_point+1
       a=f"you entered {user_choice} and computer entered {computer_choice}"
       print(a)
       b=f"you has {human_point} point and computer has {computer_point} point"
       print(b)
 elif(user_choice=="water" and computer_choice=="snake"):
       computer_point=computer_point+1
       a=f"you entered {user_choice} and computer entered {computer_choice}"
       print(a)
       b=f"you has {human_point} point and computer has {computer_point} point"
       print(b)
 elif(user_choice=="water" and computer_choice=="gun"):
       human_point=human_point+1
       a=f"you entered {user_choice} and computer entered {computer_choice}"
       print(a)
       b=f"you has {human_point} point and computer has {computer_point} point"
       print(b)
 elif(user_choice=="gun" and computer_choice=="snake"):
       human_point=human_point+1
       a=f"you entered {user_choice} and computer entered {computer_choice}"
       print(a)
       b=f"you has {human_point} point and computer has {computer_point} point"
       print(b)
 elif(user_choice=="gun" and computer_choice=="water"):
       computer_point=computer_point+1
       a=f"you entered {user_choice} and computer entered {computer_choice}"
       print(a)
       b=f"you has {human_point} point and computer has {computer_point} point"
       print(b)
 else:
       print("Wrong input") 

 no_of_chances = no_of_chances+1
print("\t \t \t \t \t Game over")
if human_point > computer_point:
     print("You won") 
elif human_point == computer_point:      
    print("Game is draw")
else:
     print("Computer won")