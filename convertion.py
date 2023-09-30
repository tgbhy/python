unites = {
    # Times
    # seconds and miliseconds
    's-ms': 1000,
    'ms-s': 0.01,
    
    # seconds & minutes
    's-min': 1/60,
    'min-s': 60,

    # minutes & hours
    'min-h': 1/60,
    'h-min': 60,

    # hours & days
    'h-day': 1/24,
    'day-h': 24,

    # days & weeks
    'day-weeks': 1/7,
    'weeks-day': 7,

    # weeks & months
    'weeks-month': 1/4.345,
    'month-weeks': 4.345,

    # months & years
    'month-year': 1/12,
    'year-month': 12,

    # lengths
    # nanometers & micrometers
    'nm-µm': 1/1000,
    'µm-nm': 1000,

    # micrometers & milimeters
    'µm-mm': 1/1000,
    'mm-µm': 1000,

    # milimeters & centimeters
    'mm-cm': 1/10,
    'cm-mm': 10,

    # centimeters & meters
    'cm-m': 1/100,
    'm-cm': 100,

    # meters & kilometers
    'm-km': 1/1000,
    'km-m': 1000
}

def convert(firstunite: str, afterunite: str, firstvalue: float) -> int | str:
    unite = firstunite + '-' + afterunite;

    if unite in unites:
        return float(firstvalue) * float(unites[unite]);
    else:
        return "Cette convertion n'existe pas !";


if __name__ == "__main__":
    firstunite = input("Quelle est la première unité (symbole) ? ");
    secondunite = input("Quelle est la seconde unitée (symbole) ? ");
    basevalue = float(input("Quelle est la valeur à transformer ? "));

    print(f'Votre résultat est: {convert(firstunite, secondunite, basevalue)}');