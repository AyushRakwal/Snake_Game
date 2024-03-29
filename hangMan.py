import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

chosen_word = random.choice(words)
words_len = len(chosen_word)

display =[]
for _ in range(words_len):
  display+="_"

end_of_game = False
lives = 6

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for pos in range(words_len):
    letter = chosen_word[pos]
    # print(f"Current Pos : {pos}\n Current letter:{letter} \n Guess Letter:{guess}")
    if(letter == guess):
      display[pos] = letter


  if guess not in chosen_word:
    lives-=1
    if lives == 0:
      end_of_game = True
      print("YoU Lose")


    print(f"{' '.join(display)}")
  print(display)

  if("_" not in display):
    end_of_game = True
    print("YOU Win")


    