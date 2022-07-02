import random
import os
import time 
import sys 
#from hangman_words import word_list
word_list =["avakado","baboon","apple","banana","orange"]
chosen_word=random.choice(word_list)
#print(chosen_word)
lives=6
#from hangman_art import logo, stages 
#print(logo)
display =[] #create blanks 
for _ in range (len(chosen_word)):
    display += "_"
print(display)
end_of_game=False
while not end_of_game==True:
  guess=input("Guess a letter: ").lower() # take input from user 
  if guess in display:
    print("you already guess")






  for i in range(len(chosen_word)):
        letter=chosen_word[i]
        #print(chosen_word[i])
        if letter==guess: # check if 
          
             display[i]= letter # assign the letter to index i 
          
        #if guess in display:
                 #print("you already guess it before")
          #else:
  if guess not in chosen_word:
    print("you guesss is not in chosen_word you loose a life")
    lives-=1
    if lives==0:
      end_of_game =True
      print("you lose ")     
  print(display)
  if "_" not in display: #end condition of game 
    end_of_game=True 
    #print(display)
    print("You Won")
    #print(stages[lives])