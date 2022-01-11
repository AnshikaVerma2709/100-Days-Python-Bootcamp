# Day 3
# Treasure hunt game


print("")
print("              \\         _")
print("             //\\       /|\\")
print("             |  \\     // |/")
print("                 \\   |/........            ")
print("                  \\  /::::::::._____________")
print("                 :|| |:::::::::|\    $$$     \      ")
print("            ...:: || |:::::::::|\\____________\\")
print("        .:::::::::|| |.:::::::::.\|_____#_____|")
print("     .::.::..:::::|| |.....::::::.|___________|:.")
print("   .::::::::::::::|| |:::::.::::::::.::::....::::.")
print(" .::::::::::::::::::::::..:::::.:::::::..:.:::::..:::..")
print("...::......:::..:....::::::;;:::..:::..::::...:::...:::...")

print("Welcome to treasure island!\n.......\n.......\nOne fine day you found a yourself on a desserted island. There are 3 directions you can head on to..\n")
a = input("Enter if you want to go left right or forward")
if(a == "left"):
  b = input("You reach a river.\nSwim or wait for boat? ")
  if(b== "swim"):
    print("Eaten by crocodile.\n GAME OVER")
  else:
    print("Ow, Snap!! There is no path ahead!\nBut! You are patient :). Hence you recieve 11$.")
elif(a== "right"):
  b = input("You are at a castle. Seems no one is inside. \nSlide inside or knock at the door?. Slide or knock? ")
  if(b == "slide" or "Slide" or "SLIDE"):
    print("Bad manners!! Demon eats you.")
  else:
    print("Fairy opens the door! You get a pretty dress and car to home!")
