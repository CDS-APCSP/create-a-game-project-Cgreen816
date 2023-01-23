import os, time

health = 100
laserGun = False
ammo = 0
grenade = 0
monsters = 0

def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome space explorer! You are the character Samuel Brett who came to the aid of a ship who put up their distress signal.")
  print()
  print()
  print("Let's get started!")
  time.sleep(3) # wait 3 seconds before moving on
  room1() # runs to send the player to cave #1

def room1():
  global laserGun, health, ammo # use the shovel variable from the top
  os.system('clear')
  if laserGun > 0:
    print("You are in the air lock. Would you like to take the corridor to your left or to your right?")
  else:
    print("You enter the ship. There is a laser gun on the ground, a corridor to your left, and a corridor to your right. What would you like to do?")
  decision = input(">>").strip().lower()
  if decision.find("gun") > -1:
    print("You pick up the laser gun, it only has one shot left")
    laserGun = True
    ammo = 1
    time.sleep(3)
    room1()
  elif decision.find("left") > -1:
    print("Fearing what might have caused the distress signal, you walk carefully down the corridor and find a dead end.")
    time.sleep(2)
    print("As you turn back, a giant space moster attacks you!")
    print("Do you flee or attack?")
    decision = input(">>").strip().lower()
    if decision.find("attack") > -1 and ammo > 0 and laserGun == True:
      print("You fire a shot at the alein and escape unscathed, returning from where you came")
    elif laserGun == False and decision.find("attack") > -1:
      print("You tried attacking the alien without a weapon")
      health -= 100
      print("Health = " + str(health))
      time.sleep(3)
      endGame("died")
    elif laserGun == False and decision.find("attack") > -1:
      print("You are out of ammo")
      time.sleep(3)
      endGame("died")
    else:
      print("You try and run away but the alien damages you on the way out.")
      health -= 50
      print("Health = " + str(health))
      print(health)
    time.sleep(3)
    room1()
  elif decision.find("right") > -1:
    print("Walking through the corridor on the right.")
    time.sleep(3)
    room2()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    os.system('clear')
    room1()
  

def room2():
  global ammo, health, laserGun, grenade 
  os.system('clear')
  print("You make your way into a new room, finding a heap of supplies on the floor and split in the path, left or right")
  print("What do you do?")
  decision = input(">>").strip().lower()
  if decision.find("supplies") > -1 or decision.find("search") > -1 or  decision.find("heap") > -1:
    os.system('clear')
    print("You find 1 energy shot, a space grenade, and a first aid kit")
    ammo += 1
    grenade += 1
    if health < 100:
      health += 25
    print()
    print("Health = " + str(health))
    print("Ammo = " + str(ammo))
    print("Grendaes = " + str(grenade))
    print()
    print("Do you go left or right?")
    decision = input(">>").strip().lower()
    if decision.find("right") > -1:
      room3()
    if decision.find("left") > -1:
      room4()
  elif decision.find("right") > -1:
    room3()
  elif decision.find("left") > -1:
    room4()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    os.system('clear')
    room2()
    

  

def room3():
  global ammo, health, laserGun, grenade
  os.system('clear')
  print("While your walking, two aliens suprise you!")
  print("escape or attack?")
  decision = input(">>").strip().lower()
  if decision.find("attack") > -1 and ammo > 0 and (laserGun == True or grenade > 0):
    print("What weapon do you use?")
    decision = input(">>").strip().lower()
    if decision.find("gun") > -1 and ammo > 1 and laserGun == True:
      print("You fire two shots at the aliens and emerge unscathed")
      time.sleep(3)
      endGame("survived")
    elif decision.find("gun") > -1 and ammo == 1 and laserGun == True:
      print("You realize you only have one shot left")
      print("You fire one shot at an alien and attempt run away from the other")
      print("the alien catches you")
      health = 0
      print("Health = " + str(health))
      time.sleep(5)
      endGame("died")
  elif laserGun == False and decision.find("attack") > -1 and grenade < 1:
    print("You tried attacking the alien without a weapon")
    time.sleep(3)
    endGame("died")
    return 
  elif laserGun == True and decision.find("attack") > -1 and ammo == 0:
    print("You are out of ammo")
    time.sleep(3)
    endGame("died")
  elif decision.find("grenade") > -1:
    print("your grendade took out all of the aliens, but damaged you 50 points")
    health -= 50
    if health < 0:
      endGame("died")
    print("Health = " + str(health))
    print()
    print("You advance to the next area")
    time.sleep(3)
    endGame("survive")      
  elif decision.find("escape") > -1:
    print("You try and run away but the aliens damages you on the way out.")
    health = 0
    print("Health = " + str(health))
    time.sleep(3)
    endGame("died")
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    os.system('clear')
    room3()

def room4():
  global ammo, health, laserGun, grenade
  os.system('clear')
  print("You enter the room and find 3 aliens surrounding you")
  print("You are forced to attack")
  if laserGun == True or grenade > 0:
    print("what weapon do you use?")
    decision = input(">>").strip().lower()
    if decision.find("gun") > -1:
      print("You do not have enough ammo for all the aliens")
      time.sleep(3)
      endGame("died")
    elif decision.find("grenade") > -1:
      print("your grendade took out all of the aliens, but damaged you 50 points")
      health -= 50
      if health < 0:
        endGame("died")
      print("Health = " + str(health))
      print("Ammo = " + str(ammo))
      print("Grendaes = " + str(grenade))
      print()
      print("You head back the way you came")
      time.sleep(3)
      room2()      
    else:
      print("Sorry, that command is not found.")
      time.sleep(3)
      os.system('clear')
      room4()
  else:
      print("You tried attacking the alien without a weapon")
      health -= 100
      print("Health = " + str(health))
      time.sleep(3)
      endGame("died")

def endGame(condition):
  os.system("clear")
  if str(condition) == "died":
    print()
    print("YOU DIED")
  if str(condition) == "survived":
    print("After surviving the aliens, you come across the crew of  the ship hiding in the engine room")
    print("Now that the aliens are gone, you and  the crew are now safe")
    print("CONGRADULATIONS")
    print()
    print("YOU WIN")
startGame()