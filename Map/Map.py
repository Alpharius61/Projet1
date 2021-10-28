# coding in utf-8

# Import
import Data as Data
import json
import os, sys
import Player.Player
import RichConsole as RC
import ImportData as ImportData
os.system('')

def MapInit():
    #  Load map element
    ImportData.LoadMapElementsFromFile()
    LoadMap()
    DrawMap()



def LoadMap():
    """
        Load map data from text file

    """
    try:
        Mapdata = []
        with open(f"Map/Map1", "r", encoding="utf-8") as MyFile:
            MapData = MyFile.readlines()

        # reset actual map
        Data.MapData = []

        # parse map data into 2D list
        # for each line in map data
        for PositionY, MapLine in enumerate(MapData):
            # define empty list for current line
            CurrentLine = []
            # for each character in line
            for PositionX, Character in enumerate(MapLine):
                # if character is not end of line
                # add it to current line list
                if Character != "\n":
                    CurrentLine.append(Character)
                    if Character == "S":
                        # this is player entry point
                        Data.PlayerData["Y"] = PositionY + 1
                        Data.PlayerData["X"] = PositionX + 1
            # add current line to map data
            Data.MapData.append(CurrentLine)

        # save text position under map
        Data.TextLine = len(Data.MapData) + 2

    except:
        print(f"\nERREUR lors du chargement de la carte")







def DrawMap():
    """
        Draw map on screen from MapData 2D list
    """

    # RC.ClearConsole()

    # each line in 2D list
    for Y, Line in enumerate(Data.MapData):
        # for each column in current line
        for X, Character in enumerate(Line):
            # get map element data from dictionnary
            # matching current character in 2D list
            MapElement = Data.MapElements[Character]
            # print map element at coordinates
            RC.ColorPrintAt(
                MapElement["Symbol"],
                MapElement["Foreground"],
                MapElement["Background"],
                Y+1,
                X+1)
