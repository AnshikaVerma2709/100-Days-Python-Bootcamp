#DAY 7 Hangman

import random

def hangman():
  let = input("Enter letter. ")
  return let


def exist(character, s_word):
  for i in range(0, len(s_word)):
    if(character == s_word[i]):
      return True
  return False


def wrong(error):
  if(error == 1):
    print(" *---------*")
    print(" |         |")
    print("           |")        
    print("           |")
  elif(error == 1):
    print(" *---------*")
    print(" |         |")
    print(" 0         |")
    print("           |")
    print("           |")

  elif(error == 2):
    print(" *---------*")
    print(" |         |")
    print(" 0         |")
    print("/          |")
    print("           |")
    print("           |")

  elif(error == 3):
    print(" *---------*")
    print(" |         |")
    print(" 0         |")
    print("/|         |")
    print(" |         |")
    print("           |")
  elif(error == 4):
    print(" *---------*")
    print(" |         |")
    print(" 0         |")
    print("/|\        |")
    print(" |         |")
    print("           |")
  elif(error == 5):
    print(" *---------*")
    print(" |         |")
    print(" 0         |")
    print("/|\        |")
    print(" |         |")
    print("/          |")
    print("           |")
  elif(error == 6):
    print(" *---------*")
    print(" |         |")
    print(" 0         |")
    print("/|\        |")
    print(" |         |")
    print("/ \        |")
    print("           |")


word_list = ["piedpiper", "bookshelf", "alligator", "branches", "gyser", "watercooler", "sanitation", "tobacco"]
word = random.choice(word_list)
print("               ___________  .         . .------------.  .          .  ___________  .         .")
print("|           | |           | |\        | |             | |\        /| |           | |\        |")
print("|           | |           | | \       | |               | \      / | |           | | \       |")
print("|           | |           | |  \      | |               |  \    /  | |           | |  \      | ")
print("|           | |           | |   \     | |               |   \  /   | |           | |   \     | ")
print("|-----------| |-----------| |    \    | |    .-------.  |    \/    | |-----------| |    \    | ")
print("|           | |           | |     \   | |    |        | |          | |           | |     \   | ")
print("|           | |           | |      \  | |             | |          | |           | |      \  | ")
print("|           | |           | |       \ | |             | |          | |           | |       \ | ")
print("|           | |           | |        \| \_____________. |          | |           | |        \| ")
print("\n\n\n")


output = " "
err = 0
err = int(err)
for i in range(0, len(word)):
  output = "_ " + output
  
print(output, "\n\n")

for i in range(0, len(word)):
  letter =  hangman()
  if exist(letter, word) == True:
    for j in range(0, len(word)):
      if(j == "_" and word[j]==letter):
        word[j] = letter
  else:
    err += 1
    wrong(err)
    if(err == 6):
      print(f"The word was: {word}")
      print("\n\nGAME OVER")
      break
