print("Démarrage du script en cours...")

def InInterval(a: float, b: float, x: float, intervalType: str):
    intervalType = intervalType.lower()

    if (intervalType == "fermé"):
        if a <= x and x <= b:
            return(True)
    elif (intervalType == "ouvert"):
        if a < x and x < b:
            return(True)
    elif (intervalType == "semi ouvert à gauche"):
        if a < x and x <= b:
            return(True)
    elif (intervalType == "semi ouvert à droite"):
        if a <= x and x < b:
            return(True)
    else:
        return(None)

    return(False)
    
def main():
    print("Nous travaillons sur les intervalles avec les valeurs a ; x et b")
    print("Vous pouvez utiliser l'infini avec inf & -inf")

    # Définition de la valeur a
    a = str(input("Quel est la valeur de a ? "))

    if a == "inf":
        a = float("inf")
    elif a == "-inf":
        a = float("-inf")
    elif a.isnumeric():
            a = float(a)
    else:
        print("a n'est pas un nombre !")
        input()
        main()
        return

    # Définition de la valeur x 
    x = str(input("Quel est la valeur de x ? "))

    if x in ("inf", "-inf"):
        print("Vous ne pouvez pas définir x sur une valeur infinie !")
        input()
        main()
        return
    
    if x.isdigit():
        x = float(x)
    else:
        print("La valeur x n'est pas un nombre !")
        input()
        main()
        return
    
    # Définition de la valeur b
    b = str(input("Quel est la valeur de b ? "))

    if b == "inf":
        b = float("inf")
    elif b == "-inf":
        b = float("-inf")
    elif b.isdigit():
        b = float(b)
    else:
        print("La valeur b n'est pas un nombre !")
        input()
        main()
        return;

    # Vérification de a et b
    if (a > b):
        print("Il y a une erreur dans votre interval : a ne peut pas être plus grand que b (a > b) !")
        return

    print("\nLes types d'intervales disponible sont : ")
    print("  - Fermé")
    print("  - Ouvert")
    print("  - Semi ouvert à gauche/droite")
    interval_type = str(input("Quel est le type que vous voulez ? "))

    if interval_type == "fermé" and (a == float("-inf") or b == float("inf")):
        print("Votre interval ne peut pas être fermé car l'un de vos nombre (a ou b) est l'infini !")
        return

    x_in_interval = InInterval(a, b, x, interval_type)
    if (x_in_interval is None):
        print("Le type n'existe pas ! Veuillez recommencer !")
        main()
        return
    else:
        if (x_in_interval is True):
            print(f"x ({x}) est contenue dans l'interval {interval_type} a;b avec a = {a} et b = {b} !")
        else:
            print(f"x ({x}) n'est pas contenue dans l'interval {interval_type} a;b avec a = {a} et b = {b}")

main()
