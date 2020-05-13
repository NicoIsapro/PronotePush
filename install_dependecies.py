#Dependencies setup for pronotePush by firelop
import os

print("[INFO/WARNING] Cette installation des dépendances automatique ne fonctionnera pas forcément,\n en fonction de votre systeme d'exploitation, de vos paramètre path etc...\n Si vous avez des érreurs le mieux est d'installer les dépendances manuellement")

def install(module):
  os.system(f"pip3 install {module}")
  
dependecies = ["Dryscrape", "Bs4", "getpass", "PySimpleGUI"]

for m in dependecies:
  print("\n\n ------------------", m, "------------------\n\n")
  show_message = True
  try:
    __import__(m) 
  except ModuleNotFoundError:
    show_message = False
    install(m)
  
  if(show_message):
    print(m, "déjà installé !")
  


input()
  
  
