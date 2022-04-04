# DAY 5 Password Generator

import random

Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '^', '*', '_', '~']

String = " "
for i in range (0, 15):
  key = random.randint(1, 2000)
  if(key%3 == 0):
    String = String + random.choice(Letters)
  elif(key%3 == 1):
    String = String + random.choice(Numbers)
  else:
    String = String + random.choice(symbols)

print(f"Your password is {String}")
