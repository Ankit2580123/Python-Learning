##Create a program of guessing a number
import random

target=random.randint(1,100)
print(target)

while True:
                    guessChoice=input("Enter your Guessing Number or Quit(Q):")
                    if(guessChoice=='Q' or guessChoice=='q'):
                                        print("You are Quited the Game, Thank You!")
                                        break
                    guessChoice=int(guessChoice) ##typecaste to integerq
                    
                    
                    if(guessChoice==target):
                                        print("Congrats! you are right guessed the target")
                                        break
                    elif(guessChoice>target):
                                        print("Please Guess to Small Number in the range of==>","1","-",guessChoice)
                                        
                    elif(guessChoice<target):
                                        print("Please Guess to Bigger Number in the range of==>",guessChoice,"-","100")
                                        
print("-------GAME OVER--------")