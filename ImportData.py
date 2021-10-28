import json
import Data as Data


def LoadPlayerFile():
   
    try :
        with open("Player/Player.json","r",encoding="utf-8") as PlayerFiles :
            Data.PlayerData= json.load(PlayerFiles)
            
    except :
        print("Erreur lors du chargement des données du personnage")


def LoadMapElementsFromFile():
    try :
        with open("Map/MapElements.json","r",encoding="utf-8") as MapFile :
           Data.MapElements = json.load(MapFile)
           
    except :
        print("Erreur lors du chargement des données de la map")

#  Load data for quests from quest file
def LoadQuestsDatasFromFile():
    try :
        with open("Quest\QuestData.json", "r", encoding="utf-8") as Myfile :
            Data.QuestsData = json.load(Myfile)
            
    except :
       print("Erreur lors du chargement des données de la quête") 



