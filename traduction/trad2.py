from textblob import TextBlob
import os
import json
import sys
import time
import subprocess
from colorama import init, Fore, Back, Style
init()

os.system('cls')
os.system('title Test tgbhy')

search = "%1$s has made the advancement %2$s%3$s%4$s"
search_replace = "%1$s a réaliser le progrès %2$s%3$s%4$s"

with open(r'allayance.mcfunction', "r", encoding="UTF-8") as file:
    data = file.read()

    data = data.replace(search, search_replace)

with open(r'allayance.mcfunction', "w", encoding="UTF-8") as file:
    file.write(data)

print("Le fichier a été édité !")