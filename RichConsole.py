import os, sys

# Variables and constants
Prefix = "\x1b["
Style_Suffix = "m"
Reset = "0"
Colors = {
    "BLACK" : "0",
    "RED" : "1",
    "GREEN" : "2",
    "YELLOW" : "3",
    "BLUE" : "4",
    "PURPLE" : "5",
    "CYAN" : "6",
    "WHITE" : "7"
}
FG_Prefix = "3"
BG_Prefix = "4"
Position_Suffix = "H"


# Functions


def ColorPrintAt(
    Text, 
    FG = "", 
    BG = "", 
    TextY = None, 
    TextX = None):
    """
        Print a text with a specific foreground, background color and position
    
        Text -> str : text to be printed
        FG -> str : Foreground color
        BG -> str : Background color
        TextY -> int : Line position
        TextX -> int : Column position
    """
    #  Separator is use to pass multiple parameters (colors for forgroud and background)
    Separator = ""
    if FG != "":
        FG = f"{FG_Prefix}{Colors[FG]}"
    if BG != "":
        BG = f"{BG_Prefix}{Colors[BG]}"
    if FG != "" and BG != "":
        Separator = ";"

    Position = ""
    if TextY != None and TextX != None:
        Position = f"{Prefix}{TextY};{TextX}{Position_Suffix}"

    print (
        f"{Position}{Prefix}{FG}{Separator}{BG}{Style_Suffix}{Text}{Prefix}{Reset}{Style_Suffix}",
        end="",
        flush=True)


def ClearConsole():
    """
        Clear the console depending on OS
    """

    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")

