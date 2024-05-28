import random as r
from pygame import mixer
mixer.init()
words = ["apple", "banana", "chair", "dog", "elephant",
         "fish", "guitar", "house", "ice cream", "juice",
         "kite", "lemon", "monkey", "nest", "orange",
         "pencil", "queen", "rainbow", "sun", "tree"]

word = r.choice(words)
temp = list(word)
for i in range(len(temp)):
    temp[i] = '_'
#******************************************************************

#******************************************************************************
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

key=int(input("Press 1 for start the game: "))
if key==1:
    print(r'''
    
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗    ██████╗ ██╗      █████╗ ██╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║    ██████╔╝██║     ███████║ ╚████╔╝ 
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    ██║     ███████╗██║  ██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                                                                     ''')
    print("\nWELCOME IN HANGMAN PLAY\n\n")
    # ***************************************************
    mixer.music.load("Fluffing-a-Duck(chosic.com).mp3")
    mixer.music.play()
    # ***************************************************
    print("WORD STORED SUCCESSFULY THEN GUESS THE WORD\n")
    print(f"the word has {len(word)} characters\n")
    for i in range(len(word)):
        print("_", end=" ")
    print("\n")
    i=0
    j=0
    #print(word)
    #while(temp!=word and j<len(HANGMANPICS)):
    while("".join(temp) != word and j < len(HANGMANPICS)):
        flag=0
        guess = input("GUESS A CHARACTER: ")
        for i in range(len(temp)):
            if word[i] == guess:
                temp[i] = guess
                flag = 1
                print("\nyes,you are in correct way\n")
        if flag == 0:
            print(HANGMANPICS[j])
            j += 1

        for m in range(len(temp)):
            print(temp[m],end="  ")
        print("\n")
        #if temp == word:
        if "".join(temp) == word:
            print("YESSS....YOU DID IT\n")
           # mixer.music.stop()
            # mixer.music.load("success-fanfare-trumpets-6185.mp3")
            # mixer.music.play()
            # while mixer.music.get_busy():
            #     mixer.time.Clock().tick(3)  # Adjust the tick rate as needed
            # mixer.music.load("success-fanfare-trumpets-6185.mp3")
            # mixer.music.play()
            print(r'''
            
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝
                                                            ''')
            exit()
        elif j==len(HANGMANPICS):
            print("TRY AGAIN LATER")
            print(r'''
            
██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          ''')
            exit()
        i+=1


