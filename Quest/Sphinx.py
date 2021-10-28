import random
import RichConsole as RC
import Player.Player as Player
import Map.Map as Map
import Data as Data
import ImportData as ImportData





def Sphinxmain():
    # Erase the consol
    RC.ClearConsole()
    ImportData.LoadQuestsDatasFromFile()
    # Variables valus assigment
    TryNumber = Data.QuestsData['sphinx']['TryNumber']
    search = Data.QuestsData['sphinx']['search']
    # Introduction text
    print(f"""
 Après avoir traversé l'île et sa jungle tu découvre une immense statue à l'image d'un sphinx. Tu t'en approche et soudain 
 il s'éveil et te met au défi : trouve les nombre que j'ai choisi, ils sont entre 0 et 100. Si tu réussi tu auras l'une 
 des trois clé
    """)
    # While to repeat the quest all at necessary
    while Data.GameOn == True :
        SearchNumber(TryNumber,search)
        Rep()
    #  Exit of the quest and back to the game's map
    RC.ClearConsole()
    Map.DrawMap()
    Player.Draw()
    

def SearchNumber(TryNumber,search):
    """
    Player search 3 random number between 0 to 100 and he have a number of test fix in the quest file

    """   
    # We search 3 numbzers
    for i in range (0,3):
       
        number = random.randint(0,100)
        TryNumber = Data.QuestsData['sphinx']['TryNumber']

        
        # Player have 20 tantative to find the number 
        while TryNumber > 0 :
        # Verification of the player input with exception gestion 
        # (while the answer of player isn't an integer he must input again)
            Enter = False
            while Enter == False :
                try :
                    PlayerAnswer = int(input("Réponse choisit : \n"))
                    Enter = True

                except :
                    print("Ta réponse ne peux être qu'un nombre réessaye")
                    continue
                

            # Testing of the player's answer 
            if PlayerAnswer > number :
                TryNumber  = TryNumber - 1
                if TryNumber == 0 :
                    break

                else:
                   print(f"Moins, il te reste {TryNumber} essais\n")
                

            elif PlayerAnswer < number :
                TryNumber  = TryNumber - 1
                if TryNumber == 0 :
                    break
                else :
                    print(f"Plus, il te reste {TryNumber} essais\n")
                
        
            else :
               
                if search == 0 :
                    print()
                    break
                     
                    
                
                else :
                    search = search -1
                    print("Tu as trouvé\n")
                    break

            
        if TryNumber == 0: 
            Data.rep = False
            break

    if search == 0 :
        Data.rep = True
        
          

          
def Rep():
    """
    Give an answer wich depend if player found all nuber or not 

    """
    if Data.rep == False :
        print("Tu as échoué.\n")
        Enter = False
        while Enter == False :
            try :
                Choix = input("Veux tu réessayer ?((o)ui/(n)on\n").lower

                if Choix == "oui" or Choix =="o" :
                    Enter = True
                    Data.GameOn = True
                
                else :
                    Data.GameOn = False
            except :
                continue
        

    elif Data.rep == True :
        print("Tu les as trouvé, je te donne cette clé, il te faudra les 2 autres pour ouvrir la porte")
        Data.KeysInventory.append(1)
        Data.SphinxQuest = True
        Data.GameOn = False
        
               

    

if __name__ == "__main__":
    Sphinxmain()
            
           
