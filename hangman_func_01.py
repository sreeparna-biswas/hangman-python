import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#hint func
def hint():
    #pass
    
    global chosen_word
    global disp_inp
    list1=[]
    if disp_inp=='y'.lower():
    
        for i in range(len(display)):
            if display[i]=='_':
                list1.append(i)
        hint_ind=random.choice(list1)
        display[hint_ind]=chosen_word[hint_ind]
        print(*display)
    

def play():
    global disp_inp
    global guess
    global chosen_word
    global display
    global lives
    print(r"""
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/                  """)

    print()
    print("WELCOME TO THE HANGMAN GAME!!!")
    print()
    print("Guess the word:-")
    #word_list = ["prepinsta", "prime", "mohan"]
    #word_list = ["the mohan"]
    
    hang_file = open("hang.txt", "r") 
    data = hang_file.read()  
    word_list = data.split("\n")  

    
    #word_list=['abacd']
    chosen_word=random.choice(word_list)
    hang_file.close()
    lives=6
    display=[]
    for i in  chosen_word:
        if i==' ':
            display.append(' ')
        else:
            display.append('_')
    print(*display)
    
    while (display.count('_')!=0):
    
        if lives>0:
            print()
            disp_inp=input("Do you want some hint? 'y'/'n': ")
            hint()
            print()
            if display.count('_')!=0:
                guess= input("Guess a letter:")[0].lower()
                guess_check()
       
        else:
            break

    if display.count('_')==0:
        print()
        print("Congratulations.You have guessed the word right.")
    else:
        print()
        print("You Lose")
        print(f"Psst! The correct word is {chosen_word}")

    print()
    inp=input("If you want to play again press 'y' else press anything to exit:").lower()
    if inp=='y':
        play()
    else:
        print()
        print("Thank you for playing.")

def guess_check():
    global chosen_word
    global guess
    global display
    global lives
    if guess in list(chosen_word) and guess not in display:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                display[i]=chosen_word[i]
        print()
        print(*display)
        #print(stages[lives])
     
    elif guess in display:
        print()
        print("Already Guessed, please choose another letter.")
        print()

    else:
        print()
        print(f"You have guessed {guess}, that's not in the word, you lose a life.")
        lives=lives-1
        print()
        print(stages[lives])
        print(*display)
   

play()
