# Imports
import RichConsole as RC
import Map.Map as Map
import Player.Player as Player
import Data as Data
import ImportData as ImportData



def Main():
    Menu()



def Menu():
    #  Main menu were player choose what he want to do
    Userchoose =""
    while Userchoose != 'Q':
        Userchoose = input("""
        (J)ouer
        (Q)uitter
     
        """).upper()

        if Userchoose == 'J':
            PlayGame()

        if Userchoose == 'Q':
            print("Au revoir\n")

def PlayGame():
    # check if the player entry is ok
    NameOk = False
    while NameOk == False :
        try :
            Data.PlayerName = str(input(f"Quel est ton nom ?\n"))
            if len(Data.PlayerName) > 0 :
                NameOk = True
        except :
            continue

    print(
    """
    Tu te réveille sur une île tropicale. Tu te releves et apercois un sac à dos contenant une carte,
    un chargeur solaire, un couteau et une bouteille.Une note te dis de résoudre les énigmes et d'aller
    tout d'abord voir le sphinx au Nord.
    """)
    Pause = input('presse une touche pour continuer')
    

    RC.ClearConsole()
    # import all files needed
    ImportData.LoadMapElementsFromFile()
    ImportData.LoadPlayerFile()
    Map.LoadMap()
    Data.PlayerData['Alive'] = True
    
    # principal loop of game 
    while Data.Action != "Q" and Data.PlayerData['Alive']== True and Data.Victory == False :
        Map.DrawMap()
        Player.Draw()
        Player.PrintPlayerStats()
        Player.ActionOfPlayer()


        
        


def ChargedGame() :
    pass


if __name__=="__main__":
    Main()