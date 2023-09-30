import yaml

# Définir l'ordre personnalisé des clés
custom_order = ["name", "description", "item", "permissionEnable", "permission", "price", "bypassVerification", "SonConfig"]

# Fonction de représentation personnalisée pour les dictionnaires
def dict_representer(dumper, data):
    return dumper.represent_mapping('tag:yaml.org,2002:map', data, flow_style=False)

# Fonction de représentation personnalisée pour les listes
def list_representer(dumper, data):
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=False)

# Charger les données YAML depuis un fichier
with open("fichier_modifie.yaml", "r") as file:
    data = yaml.safe_load(file)

# Configurer les fonctions de représentation personnalisée
yaml.add_representer(dict, dict_representer)
yaml.add_representer(list, list_representer)

# Trier les clés dans l'ordre personnalisé
sorted_data = {}
sorted_data["armorColors"] = {}
for nom_son in data:
    sorted_data["armorColors"][nom_son] = {}
    for key in custom_order:
        if key in data[nom_son]:
            sorted_data["armorColors"][nom_son][key] = data[nom_son][key]

print(sorted_data)

# Écrire les données triées dans un nouveau fichier YAML
with open("fichier_modifie_ordre.yaml", "w") as file:
    yaml.dump(sorted_data, file, sort_keys=False)