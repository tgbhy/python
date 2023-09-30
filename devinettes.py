import os;
import time;

devinettes = [
    ("Quel est le langage de programmation préféré des mineurs ? ", "ruby", "Son nom est le nom d'un minerais.")
]

def clear_console():
    os.system('cls' if os.name == "nt" else 'clear')

def startGame():
    clear_console();
    print("Démarrage du jeu en cours...");
    response = input("Voulez-vous vraiment jouer ? [Y/N] ");

    if response == "Y":
        input("Attention ! Toutes les réponses doivent être en miniscules !")
        intquestion = 0;
        while intquestion < devinettes.__len__():
            answer = input(devinettes[intquestion][0])
            if answer != devinettes[intquestion][1]:
                print("Voici un indice: " + devinettes[intquestion][2]);
                print(str(devinettes[intquestion][1]));
                answer = input(devinettes[intquestion][0]);
                if answer != devinettes[intquestion][1]:
                    print("Dommage... Vous aurez plus de chance la prochaine fois !");
                    print("Passage à la prochaine question !")
                    time.sleep(1);
                    clear_console();
                    intquestion = intquestion + 1;
                    continue;
            else:
                print("Félicitation, passage à la prochaine question !");
                time.sleep(1);
                clear_console();
                intquestion = intquestion + 1;
                continue;
    
        print("Oh, il semblerais que vous ayez terminé toutes les questions ! Bravo !!!");
        time.sleep(1);
        print("Au revoir !");
    elif response == "N":
        print("D'accord, au revoir !");
        os.system('pause');
    else:
        print("Réponse non valide, au revoir !");
        os.system('pause');

if __name__ == "__main__":
    startGame();