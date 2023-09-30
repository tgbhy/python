import yaml

with open("cosmetics.yml", 'r') as file:
    data = yaml.load(file, Loader=yaml.Loader)

if (isinstance(data, dict)):
    for type_cosm in data.keys():
        if (isinstance(data[type_cosm], dict)):
            for nom_cosm in data[type_cosm].keys():
                print(type_cosm)
                print(nom_cosm)
                print(data[type_cosm][nom_cosm]["name"])
                print(data[type_cosm][nom_cosm]["item"])
                print(data[type_cosm][nom_cosm]["unlockDefault"])
                print(data[type_cosm][nom_cosm]["permissionEnable"])
                print(data[type_cosm][nom_cosm]["permission"])
                print(data[type_cosm][nom_cosm]["price"]["enable"])
                print(data[type_cosm][nom_cosm]["price"]["coinsEnable"])
                print(data[type_cosm][nom_cosm]["price"]["coins"])
                print(data[type_cosm][nom_cosm]["price"]["levelEnable"])
                print(data[type_cosm][nom_cosm]["price"]["level"])
                print(data[type_cosm][nom_cosm]["price"]["killsEnable"])
                print(data[type_cosm][nom_cosm]["price"]["kills"])
                print(data[type_cosm][nom_cosm]["price"]["deathsEnable"])
                print(data[type_cosm][nom_cosm]["price"]["deaths"])
                print(data[type_cosm][nom_cosm]["bypassVerification"]["enable"])
                print(data[type_cosm][nom_cosm]["bypassVerification"]["unlockOnUse"])