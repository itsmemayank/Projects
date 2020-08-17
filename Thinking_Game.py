import random
print("***Welcome To Number Guess Game***")
play = True
while play == True:
    guess = int(random.randint(1,20))
    chance = 3
    print("Rules:")
    print("#You'll get only 3 chance to play")
    print("#You have to Enter no Between 1 - 20.")
    print("#If you want to play Again then Enter 'yes' else 'no'.")
    print("\n")
    while chance >= 1:
        guessing = int(input("Enter No To Be Guessed: "))
        if guessing != guess:
            print("Sorry! Try Again.")
            if chance == 1:
                chance -= 1
                print("No more Chance")
                print("\n")
                continue
            else:
                chance -= 1
                print(chance,"More Chance")
                print("\n")
                continue
            
        else:
            print("Congratulation! You won the Game.")
            print("Wonna Play Again!!!")
            Input = str(input()).upper()
            if Input == "YES":
                    play = True
            else:
                    play = False
                    break
    else:
        print("The Correct Guess was:",guess)
        print("Wonna Play Again!!!")
        Input = str(input()).upper()
        if Input == "yes":
            play = True
        else:
            play = False 
            break           