import Data as Data
import Map.Map as Map
import Player.Player as Player
import ImportData as ImportData
import RichConsole as RC

def CesarMain():
    # import data 
    ImportData.LoadQuestsDatasFromFile()
    CryptageKey()
    # repeat Decryptage while the player want or he found the answer
    Data.GameOn == True
    while Data.GameOn == True :
        Decryptage()
    # exit the quest
    RC.ClearConsole()
    Map.DrawMap()
    Player.Draw()
    


def CryptageKey():
    """
    Use the letter from  the player input to use it as the cryptage key
    
    """
    RC.ClearConsole()
    print("""
 Tu arrive à un ancien temple. Les mur sont recouvert de texte indéchiffrable écrit dans ton alphabet. 
 Au centre du temple tu trouve un autel scéllé dans lequel tu vois une clé. Dessus tu arrive à lire : presse l'une des pierre,
 le temple changera mais les anciens écris seront toujour les même. Ecris ton nom tel Cesar le codait autre fois et la clé sera
 à toi     
    """)
    Saisie = False
    while Saisie == False :
        try :
            Data.PlayerEnter = input("Saisie une lettre : ")
            if len(Data.PlayerEnter) == 1 :
                Saisie = True
                
        except:
            continue
    
    Index()
    Data.CryptageKey = Data.Index[0]
    
  
def Index() :
    """
    Check if every characters of the player input is in the alphabet, if yes the index of the letter is add to the list Index,
    if not the character is add to Index

    """
    Data.Index=[]
    Data.Alphabet = Data.QuestsData['Cesar']['Alphabet']
    #  Récupération des index des lettres de Data.PlayerEnter et des espaces
    for Character in Data.PlayerEnter :
        if Character.upper() not in Data.Alphabet :
            Data.Index.append(Character)

        else: 
            Data.Index.append(Data.Alphabet.index(f"{Character.upper()}"))
        
          
def Decryptage():
    """
    Take every characters from the player input, creat a Index with index, and take every int of the list substract the 
    cryptage key (if the int is under 0, we add 26 to restart to 26 and continue to substract). At final for all int in the
    index, print letter with the number, if there is a character wich isn't int put in the list answer. 
    If list Answer = list Good Answer its finish if else the player can retry.

    """

    print(f"Ton nom : {Data.PlayerName}")
    
    # list wich contain all caracter of the player name
    GoodAnswer= []
    for Element in Data.PlayerName:
        if type(Element) == str :
            GoodAnswer.append(Element.upper())
        else:
            GoodAnswer.append(Element)

    Data.PlayerEnter = str(input(f"Quel est le mot de passe : "))
    Index()
    

    Data.Answer = []
    for IndexElement in Data.Index :
        if type(IndexElement) == int :
            NewCharacter = IndexElement - Data.CryptageKey
            if NewCharacter < 0 :
                NewCharacter = NewCharacter + 26
            Data.Answer.append(Data.Alphabet[NewCharacter])
        
        else :
            Data.Answer.append(IndexElement)
    
    # if the the player answer is good
    if GoodAnswer == Data.Answer :
        print("Bravo ! Tu as trouvé le code")
        Data.KeysInventory.append(1)
        Data.CesarQuest = True
        Data.GameOn = False
    
    
    else : 
        
        Retry = input("C'est faux, veux-tu réessayer : (o)ui/(n)on").upper()
        if Retry == 'O' or Retry =='OUI':
            Data.GameOn == True
        
        else:
            Data.GameOn == False
            

        



if __name__=="__main__":
    CesarMain()