from textblob import TextBlob
import os
import json
import sys
import time
import subprocess
from colorama import init, Fore, Back, Style
init()

def main():
    os.system("cls")
    os.system("title Merci de choisir une option")
    print(Fore.MAGENTA + "▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄ █▀▀ █░░ █▀▀█ ▀▀█▀▀ █▀▀ ")
    print(Fore.MAGENTA + "░░█░░ █▄▄▀ █▄▄█ █░░█ ▀▀█ █░░ █▄▄█ ░░█░░ █▀▀ ")
    print(Fore.MAGENTA + "░░▀░░ ▀░▀▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ")

    inp = int(input(f'{Fore.RESET}Bienvenue dans le traducteur de fichier !\n\nQue voulez vous faire ?\n\n{Fore.CYAN}1. {Fore.GREEN}Traduire un seul fichier .json\n{Fore.CYAN}2. {Fore.GREEN}Traduire les fichiers json d\'un dossier en même temps\n\n{Fore.YELLOW}Votre choix : {Fore.CYAN}'))
    if inp == 1:
        translate_fichier()
    elif inp == 2:
        translate_all_files()
    else:
        print("Veuillez entrer un nombre valide !")
        main()

def translate_all_files():
    # Récupérer le chemin du dossier courant
    current_dir = os.getcwd()
    # Pour chaque fichier dans le dossier courant
    nb_fichier = 0
    for file in os.listdir(current_dir):
        # Si le fichier a l'extension '.json'
        if file.endswith('.mcfunction'):
            nb_fichier += 1
    nb_trad = 0
    for file in os.listdir(current_dir):
        nb_trad += 1
        os.system(f'title Fichier {nb_trad}/{nb_fichier + 1}')
        # Si le fichier a l'extension '.json'
        if file.endswith('.mcfunction'):
            # Appeler la fonction de traduction existante pour ce fichier
            translate_fichier(file)
    print('\n\nNous avons fini de traduire tous les fichiers !')

def translate_fichier(fichier):
    # si le fichier est défini
    if fichier is None:
        fichier = input(print("Quel fichier voulez vous traduire ?"))
    else:
        if os.path.isfile(fichier):
            os.system("cls")
            with open(fichier, "r", encoding="utf-8") as f:
                data = f.read()

                obj = json.loads(data)
                text = obj['display']['description']['translate']
                
                blob = TextBlob(text)
                try:
                    translated = blob.translate(from_lang="en", to="fr")
                    if "Craquez" in translated:
                        translated = translated.replace("Craquez", "Craftez")

                except:
                    return
                print(f'{Fore.GREEN}============================================================')
                print(f'{Fore.RESET}Fichier : {Fore.LIGHTBLUE_EX}{fichier}\n')
                print(f'{Fore.RESET}Anglais : {Fore.LIGHTBLUE_EX}{text}')
                print(f'{Fore.RESET}Français : {Fore.LIGHTBLUE_EX}{translated}')
                print(f'{Fore.GREEN}============================================================')
                is_good = input(f'{Fore.RESET}Voulez-vous garder la traduction ? (O/N) : ')
                if is_good == "N":
                    trad = str(input(f'\nQuelle traduction voulez vous mettre :\n=> {Fore.LIGHTBLACK_EX}'))
                    obj['display']['description']['translate'] = str(trad)
                    with open(fichier, "w", encoding="utf-8") as f:
                        json.dump(obj, f, indent=4)
                    os.system(f'title Dernière traduction effectué : {trad}')
                else:
                    print(f"Ok, on garde la traduction !")
                    obj['display']['description']['translate'] = str(translated)
                    with open(fichier, "w", encoding="utf-8") as f:
                        json.dump(obj, f, indent=4)
                    os.system(f'title Dernière traduction effectué : {translated}')

        else:
            print("Le fichier n'existe pas")



if __name__ == "__main__":
    main()