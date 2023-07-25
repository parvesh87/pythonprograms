import random
while True:
    a=(random.randint(1,6))
    n=int(input("enter the number:"))
    if (n>=1)and(n<=5):
        if(a==n):
            print("you win")
            break
        else:
            print("you loss the game")
    
