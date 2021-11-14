n=0
e=["Puducherry"]
b=["+------+\n|\n|\n|\n|\n|\n|\n|\n|______\n","\n+------+\n|      |\n|      O\n|\n|\n|\n|\n|\n|\n|______","\n+------+\n|      |\n|      O\n|      |\n|      |\n|\n|\n|\n|\n|______","\n+------+\n|      |\n|      O\n|     /|      \n|      |\n|\n|\n|\n|\n|______","\n+------+\n|      |\n|      O\n|     /|\      \n|      |\n|\n|\n|\n|\n|______","\n+------+\n|      |\n|      O\n|     /|\      \n|      |\n|     /\n|\n|\n|\n|______","\n+------+\n|      |\n|      O\n|     /|\      \n|      |\n|     / \ \n|\n|\n|______"]      
print("     **HANGMAN**\n\n In this game you have to guess a union territory of India.\n")
while n<=6:
     choice=input("Enter a union territory: ")
     if choice in list(e):
         print('\nYou Won the Game.')
         break
     elif choice not in list(e):
         print(b[n])
         if n==6:
             print('\nSorry You lost the Game.')
     n+=1
