import ruamel.yaml

def replace_keys(dataSection):
    if isinstance(dataSection, dict):
        for key, value in list(dataSection.items()):
            if key == "Nom":
                dataSection["name"] = value
                del dataSection[key]
            elif key == "Description":
                dataSection["description"] = value
                del dataSection[key]
            elif key == "Item":
                dataSection["item"] = value
                del dataSection[key]
            elif key == "BypassCheckForUsePourTous":
                dataSection["bypassVerification"] = {
                    "enable": value["Actif"],
                    "unlockOnUse": value["UnlockIfUse"]
                }
                del dataSection[key]
            elif key == "Permission":
                dataSection["permissionEnable"] = value["actif"]
                dataSection["permission"] = value["permission"]
                del dataSection[key]
            elif key == "Achetable":
                dataSection["price"] = {
                    "enable": value["Actif"],
                    "coinsEnable": value["PrixEnable"],
                    "coins": value["Prix"],
                    "levelEnable": value["NiveauMinEnable"],
                    "level": value["NiveauMin"],
                    "killsEnable": value["KillsMinEnable"],
                    "kills": value["KillsMin"],
                    "deathsEnable": value["MortsMinEnable"],
                    "deaths": value["MortsMin"]
                }
                del dataSection[key]
            else:
                replace_keys(value)
    elif isinstance(dataSection, list):
        for item in dataSection:
            replace_keys(item)

# Charger les données YAML depuis le fichier en conservant l'ordre des clés
yaml = ruamel.yaml.YAML()
with open("toTransform.yml", "r") as file:
    data = yaml.load(file)

# Remplacer les clés dans les données YAML
if (isinstance(data, dict)) :
    for nom_son in data.keys():
        replace_keys(data[nom_son])

# Écrire les données modifiées dans un nouveau fichier YAML en conservant l'ordre des clés
with open("fichier_modifie.yaml", "w") as file:
    yaml.dump(data, file)