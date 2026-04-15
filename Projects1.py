#number guessing game program
import random
c=random.randrange(1,20)
userinput=int(input("Enter your guess number:  "))
if userinput>c:
    print("Computer guess number is:  ",c)
    print("Your guess number is too high")
elif c>userinput:
    print("Computer guess number is:  ",c)
    print("Your guess number is  too low")
else:
    print("Computer guess number is:  ",c)
    print("Your guess number is equal")