from math import pi, sqrt, factorial, pow, cos, acos, sin, asin, tan, atan;

def calculate(calc: str) -> float | str:
    try: 
        result = eval(calc);
    
        return result;
    except:
        return "Votre calcul n'est pas bon !";

if __name__ == "__main__":
    print("\033[93mInformations:")
    print("  - Les opérations disponibles sont '+', '-', '/', '*' et factorielle avec factorial(votre nombre)")
    print("  - Les puissances peuvent être utilisé via pow(nombre de départ, puissance)")
    print("  - Les racines carré se calcule via sqrt(votre calcul)")
    print("  - PI peut être utilisé via 'pi'")
    print("  - La trigonométrie peut être utilisé par (les () contiennent le nombre) cos(), acos(), sin(), asin(), tan(), atan()")
    print("\n" + "\033[0m")
    want = True;
    while want == True:
        print(calculate(input("Spécifier un calcul à faire: ")));
        want = input("Voulez-vous refaire un calcul ? [Y/N] ");
        while want != "Y" and want != "N":
            want = input("Voulez-vous refaire un calcul ? [Y/N] ");
        if want == "Y":
            want = True
        elif want == "N":
            want = False

    print("Au revoir !");