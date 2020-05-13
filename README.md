# Pronote Push
Petit code en Python 3 qui permet de recevoir des notifications dans la console lorsqu'une nouvelle note arrive sur Pronote, only linux car nécessite Dryscrape qui lui même nécessite webkit-server qui est codé pour un système linux uniquement.

Voir sur le site de dryscrape le 'script' d'install des modules nécessaires, c'est rapide !
Il faut déjà 4 notes sur Pronote, si c'est pas le cas modifiez le code a votre guise.

Enregistre les logins et les anciennes notes, dès que le script est lancé il récupère toutes les 2 minutes les infos de pronote.

# Modules bruts nécessaires : 
- Dryscrape
- Bs4 
- getpass
- PySimpleGui

# ToDo : 
- Optimisation 
