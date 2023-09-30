import sys
import os

firstSymbol = "X"
secondSymbol = "O"

def main():
    print("Bienvenue dans le jeu du morpion !")
    print("Démarrage du jeu en cours...")

    print("Le joueur 1 est représenté par X et le joueur 2 est représenté par O !")

    start_game(True)


def start_game(finish: bool):
    if finish is True:
        gameList = {
            "1;1": " ",
            "1;2": " ",
            "1;3": " ",
            "2;1": " ",
            "2;2": " ",
            "2;3": " ",
            "3;1": " ",
            "3;2": " ",
            "3;3": " "
        }

        showCurrentGame(gameList)
        askForPlay(False, "X", gameList)
        return
    else:
        print("Vous êtes déjà en jeu !")
        return


def askForPlay(finish: bool, symbol: str, gameList: dict):
    if finish is True:
        relaunchGame = str(
            input("La partie est finit ! Voulez-vous refaire une partie ? [Y/N] "))

        if relaunchGame == "Y":
            start_game(False)
        elif relaunchGame == "N":
            sys.exit()
        else:
            print("Veuillez rentrer O ou N comme valeur ! :v")
            askForPlay(finish, symbol, gameList)
    else:
        column = setupValue("Dans quel colonne voulez-vous mettre votre symbole ?", "La colonne n'est pas un nombre !", "La colonne ne peut pas être inférieur à 0 ou supérieur à 9 !")
        line = setupValue("Dans quel ligne voulez-vous placer votre symbole ?", "La ligne n'est pas un nombre !", "La ligne ne peut pas être inférieur à 0 ou supérieur à 9 !")

        if gameList[f"{column};{line}"] != " ":
            print("Veuillez rentrez une nouvel valeur ! Cette case est déjà remplie !")
            askForPlay(finish, symbol, gameList)
        else:
            gameList[f'{column};{line}'] = symbol

            win = check_winner(gameList)

            if win != None:
                showCurrentGame(gameList)
                print(f'{win} a gagné la partie ! Bravo à lui/elle !')
                askForPlay(True, symbol, gameList)
                return

            showCurrentGame(gameList)
            if symbol == firstSymbol:
                symbol = secondSymbol
            else:
                symbol = firstSymbol
                
            askForPlay(finish, symbol, gameList)

def setupValue(firstmessage: str, errormessage: str, outofboundserror: str) -> int:
    value = str(input(firstmessage))

    if value.isnumeric() == False:
        print(errormessage)
        while value.isnumeric() == False:
            value = str(input(firstmessage))

        value = int(value)
        if value > 3 or value < 1:
            print(outofboundserror)
            return setupValue(firstmessage, errormessage, outofboundserror)
        else:
            return value
    else:
        return value

def check_winner(gameList) -> str | None:
    # Vérifier les combinaisons horizontales
    for i in range(1, 4):
        if gameList[f"{i};1"] == gameList[f"{i};2"] == gameList[f"{i};3"] != " ":
            return gameList[f"{i};1"]

    # Vérifier les combinaisons verticales
    for i in range(1, 4):
        if gameList[f"1;{i}"] == gameList[f"2;{i}"] == gameList[f"3;{i}"] != " ":
            return gameList[f"1;{i}"]

    # Vérifier les combinaisons diagonales
    if gameList["1;1"] == gameList["2;2"] == gameList["3;3"] != " ":
        return gameList["1;1"]
    if gameList["1;3"] == gameList["2;2"] == gameList["3;1"] != " ":
        return gameList["1;3"]

    # S'il n'y a pas de gagnant
    return None

def showCurrentGame(currentGame: dict) -> None:
    os.system("clear")
    print(f"{currentGame['1;1'] or ' '}|{currentGame['2;1'] or ' '}|{currentGame['3;1'] or ' '}")
    print("-|-|-")
    print(f"{currentGame['1;2'] or ' '}|{currentGame['2;2'] or ' '}|{currentGame['3;2'] or ' '}")
    print("-|-|-")
    print(f"{currentGame['1;3'] or ' '}|{currentGame['2;3'] or ' '}|{currentGame['3;3'] or ' '}")

main()
