import random;

def generatePassword(lenght: int):
    carachters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890&é'(-è__çà)=+{}[]"
    password = [];
    for x in range(lenght):
        i = random.randrange(0, carachters.__len__())
        password.append(carachters[i])

    return ''.join(str(e) for e in password);

print("Votre mot de passe généré est: " + generatePassword(int(input("Quel taille de mot de passe voulez-vous ? "))));