import random


print('Welcome To The Guess The Number !!! ')
Computerno=random.randint(1,10)
Count=0
while Computerno:
    player=int(input('Enter a no. :'))
    if(Computerno==player):
        print(f'You Total try is :{Count} And Computer Number is {Computerno} ')
    elif(Computerno<player):
        print("You Number is Greater try again")
        Count+=1
    elif(Computerno>player):
        print("You Number is Lesser try again")
        Count+=1
    
