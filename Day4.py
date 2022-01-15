import random 

print("")
opt = ["Stone","Paper","Scissor"]
user = int(input("Enter 0 for stone, 1 for paper and 2 for scissor. "))
print("\nyou chose", opt[user])

randommed = random.randint(0,2)
print("Computer chose ", opt[randommed])
if(user == 0):
  if randommed == 0:
    print("Draw")
  elif randommed == 1:
    print("computer won")
  else:
    print ("you won")
elif(user == 1):
  if(randommed == 1):
    print("Draw")
  elif randommed == 2:
    print("computer won")
  else :
    print ("you won")
else:
  if randommed == 2:
    print("Draw")
  elif randommed == 0:
    print("computer won")
  else :
    print ("you won")
