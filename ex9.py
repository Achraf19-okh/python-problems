import random 
colors = ["white","red","green","black","blue","orange"]

while True:
     color = colors[random.randint(0,len(colors)-1)]
     guess = input("I'am thinking about a color can u guess it ")
 
    while True:
         if (color = guess.lower()):
              break
         else:
             guess = input("Nope try again : ")

    print("you guessed it! i was thinking about" , color)

    play_again = input("Let's play again? Type 'no' to quit.")
    
    if play_again.lower() == 'no':
          break
        
print("It was fun, thanks for playing!")
