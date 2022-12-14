# Haunted House with python
import time

def welcome():
  print("              /\\")
  print("             /  \\")
  print("      /\    /    \\ ")
  print("     /  \  /      \ ")
  print("    /    \/        \_/\\")
  print("   /     Welcome to    \\")
  print("  /                     \\")
  print("  |  the Haunted House! |")
  print("  |     ____     ___    |")
  print("  |    |    |   |___|   |")
  print("__|____|____|___________|__")
  print("")
  time.sleep(1)
  
welcome()

def showInstructions():
    print('''  
Commands:
  use [item] eg: use key 
  
  shoot[enemy] eg: shoot zombie
   
  go [direction] eg: go north
  
  get [object] eg: get bandage
''')
    
health= 100

def showStatus():

  print('You are in the ' + currentRoom)
  print (rooms[currentRoom]['desc'])
  print("Inventory : " + str(inventory))
  print("Your health is",health)
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")


    
inventory = []

monster=[]

rooms = {

            'Hall' : {'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  "north":"Bed Room",
                  'item'  : 'shotgun',
                  'monster'  : '', "desc":"No one has been here for a while",
                },        

            'Kitchen' : { 'north' : 'Hall',
                  "item":"golden_crown",
                  'monster'  : 'zombie',"desc":"Dead bodies scatter the floor",                        
                },
                
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'key',
                  'monster'  : 'zombie',"desc":"Old painting hangs on the wall",    
                },
                
            'Garden' : { 'north' : 'Dining Room',
            'monster'  : '', "desc": "There is a locked gate here",
                },

        'Bed Room' : {'south' : 'Hall',
            'item'  : 'bandage',
            'monster'  : 'ghoul',"desc":"There is blood all over the bed ",  
              },        
         }

currentRoom = 'Hall'

showInstructions()

while True:

  showStatus()                  

  move = ''
  while move == '':  
    move = input('>')           
    
  move = move.lower().split()   

  if move[0]=="shoot":  
      if "monster"in rooms[currentRoom] and move[1] in rooms[currentRoom]['monster'] and "shotgun" in inventory :
          del rooms[currentRoom]['monster']
          print( "you killed the", move[1])
          rooms[currentRoom].update({"monster":"dead"},)
        
      else:
          print("you cannot attack " )
          

      
  if move[0]=="use":
      
      
      if "bandage" in inventory and move[1]== "bandage":
          heal=40
          health=min(100,health+heal)
          inventory.remove("bandage")
          print("you recovered 40 health (max 100)")

      elif "key" in inventory and move[1]== "key" and "golden_crown" in inventory and currentRoom=="Garden":     
         print("you escape with the loot, you retire in style, you win!!  ")
         break    
              
          
      elif "key" in inventory and move[1]== "key" in inventory and currentRoom=="Garden":
         print("you escape the house but die a pauper, you lose ")
         break

      

      else:
          print("can't use that")

      
    
  if move[0] == 'go':
      if move[1] in rooms[currentRoom]:
          currentRoom = rooms[currentRoom][move[1]]
      else:
          print('You can\'t go that way!')

  if move[0] == 'get' :
          
      if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          inventory += [move[1]]
          print(move[1] + ' got!')
          del rooms[currentRoom]['item']
     
      else:
          print("Can\'t get that")
        
  if 'zombie' in rooms[currentRoom]['monster']:
      print("A zombie attack you !!!")
      health=health-30

  if 'ghoul' in rooms[currentRoom]['monster']:
      print('A ghoul attack you !!!')
      health=health-20
  

  if health <= 0:
      print("you are dead")
      break
        