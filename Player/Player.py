# coding: utf-8

# imports
import Data as Data
import RichConsole as RC
import Map.Map as Map
import Quest.Sphinx as Sphinx
import Quest.CesarCode as Cesar
import Quest.FizzBuzz as FizzBuzz


# function
def ActionOfPlayer():
   
    """
        Moves player in specified direction or an other action
        Action -> str : Action wich player want (move, search in inventory or sleep)
    """
    
    
    RC.ColorPrintAt("Que fais tu : H(Haut) B(Bas) G(Gauche) D(Droite) I(Inventaire) S(Dormir) Q(Quitte) ", TextY=35,TextX=0)

            
    Ok = False
    while Ok == False :
        try:
            Data.Action = input(f"").upper()

            if Data.Action == "I":
                Ok = True
                PlayerInventory()
            elif Data.Action == "S":
                Ok = True
                PlayerSleep()
                              
            elif Data.Action == 'H'or Data.Action == 'B' or Data.Action == 'G' or Data.Action == 'D'  :
                Ok = True        
                Data.Message = f"Le joueur se déplace vers {Data.Action}"
            
            elif Data.Action == 'Q':
                RC.ClearConsole()
                return
            
            else :
               Ok = False
               
               
        except :
            pass        

    # save actual player position
    PositionY = Data.PlayerData["Y"]
    PositionX = Data.PlayerData["X"]

    # calculate new player position

    if Data.Action == "H":
        PositionY -= 1
    elif Data.Action == "B":
        PositionY += 1
    elif Data.Action == "G":
        PositionX -= 1
    elif Data.Action == "D":
        PositionX += 1
   
    # check if movement is valid
    MapElementAtPlayerPosition = Data.MapData[PositionY - 1][PositionX - 1]
    MapElementData = Data.MapElements[MapElementAtPlayerPosition]
    
    # chek if door is open
    if len(Data.KeysInventory)== 3 :
        Data.MapElements["P"]["CanWalk"] = True

    #  check if the player can walk on this direction
    if MapElementData["CanWalk"]:
        Draw(True)
        Draw()
        Data.PlayerData["Y"] = PositionY
        Data.PlayerData["X"] = PositionX
        # Down player's stats
        Data.PlayerData['Hunger'] -= 2
        Data.PlayerData['Thirst'] -= 2
        Data.PlayerData['Stamina'] -= 4
        
        # check player's stat and lauch function wich is necessary
        if Data.PlayerData['Stamina'] <= 0 :
            PlayerSleep()
        if Data.PlayerData['Hunger'] <= 0 or Data.PlayerData['Thirst'] <= 0 :
            PlayerDeath()
        
        # check if the zone start a quest 
        elif MapElementData["Name"] == "Sphinx" and Data.SphinxQuest == False :
            Sphinx.Sphinxmain()
        elif MapElementData["Name"] == "Cesar" and Data.CesarQuest == False :
            Cesar.CesarMain()
        elif MapElementData["Name"] == "FizzBuzz" and Data.FizzBuzzQuest == False :
            FizzBuzz.FizzBuzzMain()

        # check if the player go on a food or a drink case 
        elif MapElementData["Name"] == "Pig" and len(Data.HungryInventory) < 5 :
            FoodFull = 5-len(Data.HungryInventory)
            for food in range(0,FoodFull) :
                Data.HungryInventory.append(1)
        elif MapElementData["Name"] == "eau" and len(Data.WaterInventory) < 5 :
            WaterFool = 5-len(Data.WaterInventory)
            for water in range(0,WaterFool) :
                Data.WaterInventory.append(1)
        
        # check if the player can go on the door case         
        elif MapElementData["Name"] == "Door" and  MapElementData["CanWalk"] == True:
            Data.Victory = True
            RC.ClearConsole()
            print("Félicitation tu as gagné")
            return

    else:
        # obstacle
        Data.Message += f"\x1b[9;59H Aïe, {MapElementData['Name']} !"
        
 
def PrintPlayerStats():
    """
    print all stats of the player 

    """
    
    RC.ColorPrintAt(f"Faim : {Data.PlayerData['Hunger']}",FG="WHITE",BG="BLACK",TextY=2,TextX=60)
    RC.ColorPrintAt(f"Soif : {Data.PlayerData['Thirst']}" ,FG="WHITE",BG="BLACK",TextY=3,TextX=60)
    RC.ColorPrintAt(f"Fatigue : {Data.PlayerData['Stamina']}",FG="WHITE",BG="BLACK",TextY=4,TextX=60)
    RC.ColorPrintAt(f"🥃 : {len(Data.WaterInventory)}",FG="WHITE",BG="BLACK",TextY=5,TextX=60)
    RC.ColorPrintAt(f"🍖 : {len(Data.HungryInventory)}",FG="WHITE",BG="BLACK",TextY=6,TextX=60)
    RC.ColorPrintAt(f"🗝️ : {len(Data.KeysInventory)}",FG="WHITE",BG="BLACK",TextY=7,TextX=60)
    RC.ColorPrintAt(f"{Data.Message}",FG="WHITE",BG="BLACK",TextY=8,TextX=60)
    


def Draw(Erase = False):
    """
        Draw player on map
    """

    Symbol = Data.PlayerData["Symbol"]
    FG = Data.PlayerData["Forground"]
    BG = Data.PlayerData["Background"]


    MapElement = Data.MapElements[
        Data.MapData[Data.PlayerData["Y"] - 1]
        [Data.PlayerData["X"] - 1]]
    # check if player is beeing erased
    if Erase:
        Symbol = MapElement["Symbol"]
        FG = MapElement["Foreground"]
        BG = MapElement["Background"]

    # draw symbol at right place
    RC.ColorPrintAt(
        Symbol,
        FG,
        BG,
        Data.PlayerData["Y"],
        Data.PlayerData["X"],
        )


def PlayerDeath():
    """
    stop the game when the player lose

    """
    RC.ClearConsole()
    print(f'Vous êtes morts')
    Pass = input("Presse une touche pour revenir au menu principal")
    Data.PlayerData['Alive'] = False


def PlayerInventory():
    """
    manage the inventory of the player

    """
    
    RC.ColorPrintAt("\x1b[35MQue veux faire ? : M(Manger), B(Boire), R(Rien)", TextY=35,TextX=0)
    Ok = False
    while Ok == False :
        try :
            Choice = input("").upper()
            
            if Choice =="M":
                Eat = int(input("Combien de viande veux tu manger ? "))
                if Eat > len(Data.HungryInventory) :
                    Eat = len(Data.HungryInventory)
                
                for i in range (0,Eat) :
                    del Data.HungryInventory[-1]
                    Data.PlayerData['Hunger'] += 10
                
                if Data.PlayerData['Hunger'] > 100 :
                    Data.PlayerData['Hunger'] = 100
                
                Ok = True
                
            
            elif Choice =="B" :
                Drink = int(input("Quelle quantité d'eau veux tu boire ? "))
                
                if Drink > len(Data.WaterInventory) :
                    Drink = len(Data.WaterInventory)
                
                for i in range (0,Drink) :
                    del Data.WaterInventory[-1]
                    Data.PlayerData['Thirst'] += 10
                
                if Data.PlayerData['Thirst'] > 100 :
                    Data.PlayerData['Thirst'] = 100
                
                Ok = True
        
            elif Choice =="R":
                Ok = True
                pass

        except :
            pass
    
def PlayerSleep():
    """
    permit to the player to reload his stamina

    """
    RC.ColorPrintAt("\x1b[35MQue veux faire ? : D(Dormir) R(Rien)", TextY=35,TextX=0)
    Ok = False
    while Ok == False :
        try :
            Choice = input("").upper()
            if Choice == "D" :
                Ok = True
                Sleep = int(input("Combien de temps veux tu dormir ? "))
                for i in range (Sleep) :
                    Data.PlayerData['Stamina'] += 10
                    Data.PlayerData['Thirst'] -= 2
                    Data.PlayerData['Hunger'] -= 2
                    if Data.PlayerData['Stamina'] >= 100:
                        break
            else :
                Ok = True
                pass
        except :
            pass