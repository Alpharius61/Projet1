import Data as Data
import Map.Map as Map
import Player.Player as Player
import ImportData as ImportData
import RichConsole as RC
import random


def FizzBuzzMain():
    # Clear the console
    RC.ClearConsole()
    Data.GameOn = True
    FizzBuzzText()
    # repeat the quest as the player want or he win
    while Data.GameOn == True :
        GamersList ()
        FizzBuzz()
        Result()
    # exit the quest
    RC.ClearConsole()
    Map.DrawMap()
    Player.Draw()

def FizzBuzzText():
    print(
    """
    Tu arrive dans une clairière ou des singes joue à un jeu que tu connais déjà : le Fizz'Buzz. Un singe qui semble être 
    le chef t'invite à te joindre à eux et si tu gagne tu obtiendras une clé de la porte.
    
    """
    )
def GamersList ():
    """
    Creat the list of gamer

    """
    ImportData.LoadQuestsDatasFromFile()
    Data.ListOfGamer = list(Data.QuestsData["Fizz'Buzz"].keys())
    Data.ListOfGamer.append(Data.PlayerName)


def FizzBuzz():
    """
    Determine for each gamer, with a random system, if the gamer is delete or not of the gamer list
    
    """
    # import player data for know his chance to tell the good answer 
   
    ImportData.LoadPlayerFile()
    
    # Test answer for each gamer, if it's false he is delete from the gamer list  
    while len(Data.ListOfGamer) != 1 and Data.PlayerName in Data.ListOfGamer :
        for Gamer in Data.ListOfGamer :
            Answer = random.randint(0,100)
            # test of the player answer
            if Gamer == Data.PlayerName :
                if Answer > Data.PlayerFiles['Chance'] :
                    Data.ListOfGamer.pop(Data.ListOfGamer.index(Gamer))
                    print("Tu es éliminé")
            
            #  test for each gamer other than the player 
            elif Answer > Data.QuestsData["Fizz'Buzz"][Gamer] :
                Data.ListOfGamer.pop(Data.ListOfGamer.index(Gamer))
                print(f"{Gamer} est éliminé")


def Result() :
    """
    print an answer in fonction the win or lose of the player

    """
    if Data.PlayerName in Data.ListOfGamer and len(Data.ListOfGamer)== 1 :
        print("Tu as gagné et récupère la clé des singes")
        Pause = input(f"\n presse Enter pour continuer")
        Data.KeysInventory.append(1)
        Data.FizzBuzzQuest = True
        Data.GameOn = False
        
    
    else:
        Valid = False
        while Valid == False:
            try :
                Choice = input("Les singes ont gagné, veux tu réesseyer ? (O)ui/(N)on \n").upper()
                if Choice == 'O' or Choice == 'OUI':
                    Valid = True

                elif Choice == 'N' or Choice == 'NON':
                    Valid = True
                    Data.GameOn = False
            except :
                continue



if __name__=="__main__":
    FizzBuzzMain()
