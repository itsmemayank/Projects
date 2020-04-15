import random
play = True
while play == True:
    print("1----->Rock\n2----->paper\n3----->scissor\n")
    myVal = int(input("Enter  your value  "))
    com = random.randint(1,4)
    
    if myVal > com:
        print("You Win")
    elif com > myVal:
        print("You Lose")
    elif myVal == com:
        print("Draw")
    else:
        print("Invalid value entered")
    
    myVal = input("\nPlay Again\n").lower()
    if myVal == "y":
        play = True
    else:
        play = False