#Pronote Push Service 1.0
# Developpe par Nico Isapro
# Interface DOS pour python 3
# Lire le fichier readme

import sys
import os
import time
import dryscrape 
import shelve
import getpass
import bs4

print ("")  
print ("  _   _   _                    ___                                      ")                                                                                       
print (" | \ | | (_)   ___    ___     |_ _|  ___    __ _   _ __    _ __    ___  ")                                                                                            
print (" |  \| | | |  / __|  / _ \     | |  / __|  / _` | | '_ \  | '__|  / _ \ ")                                                                                            
print (" | |\  | | | | (__  | (_) |    | |  \__ \ | (_| | | |_) | | |    | (_) |")                                                                                            
print (" |_| \_| |_|  \___|  \___/    |___| |___/  \__,_| | .__/  |_|     \___/")   
print ("                                                  |_|                  ") 
print ("")  
print ("              Pronote Push Service V1.0 - Lycée Louis Vincent                  ")     
print ("")          
 
 # PARTIE IDENTIFIANTS ETC 

bdd = "login.dat"
bdn = "notes.dat"

if os.path.isfile(bdd): # Si fichier présent
 d = shelve.open(bdd)
 username = d['username']
 password = d['password']
 print ("Compte enregistré : ", username)
 print ()
 d.close()

else:    # Sinon, on demande les identifiants 
 username = input("Nom d'utilisateur Place : ")
 password = getpass.getpass("Mot de passe (non affiché par sécurité) :")
 print()
# On sauvegarde tout ça 
 d = shelve.open(bdd)
 d['username'] = username
 d['password'] = password
 d.close()
 
 # PARTIE LOGIN PLACE #
while 1:
 sess = dryscrape.Session(base_url = 'https://www.ent-place.fr/CookieAuth.dll?GetLogon?curl=Z2F&reason=0&formdir=5') #MODIFIER AVEC VOTRE ENT SI BESOIN
 sess.set_header('Accept','text/html,application/xhtml+xml application/xml;q=0.9,image/webp,*/*')

 sess.visit('/')

  # IDENTIFIANTS #
 name = sess.at_xpath('//*[@id="username"]')
 name.set(username)
 pid = sess.at_xpath('//*[@id="password"]')
 pid.set(password)

  # ENVOI DES IDENTIFIANTS 
 name.form().submit()

# FAKE HEADER #
 sess.set_header('User-agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)       Chrome/50.0.2661.102 Safari/537.36')
 sess.set_attribute('javascript_can_open_windows', True)

# PARTIE PRONOTE #
 sess.visit('https://0570058d.index-education.net/pronote/')          #MODIFIER AVEC VOTRE LIEN PRONOTE
 time.sleep(4)  # Ne pas modifier cette ligne


# PARSING #
 soup = bs4.BeautifulSoup(sess.body(), "lxml")
 Note1 = soup.find('div', id="GInterface.Instances[1]_notes_0")
 Note2 = soup.find('div', id="GInterface.Instances[1]_notes_1")
 Note3 = soup.find('div', id="GInterface.Instances[1]_notes_2")
 Note4 = soup.find('div', id="GInterface.Instances[1]_notes_3") 


# PARTIE TRAITEMENT #
 if os.path.isfile(bdn): # Si fichier présent on compare les notes
  d = shelve.open(bdn)
  PNote1 = d['ANote1']
  PNote2 = d['ANote2']
  PNote3 = d['ANote3']
  PNote4 = d['ANote4']
  d.close()
  if PNote1 != Note1.get('aria-label'):   # A OPTIMISER...
   print ("Nouvelle note !")
   print (Note1.get('arial-label'))
  elif PNote2 != Note2.get('aria-label'):
   print ("Nouvelle note !")
   print (Note2.get('aria-label'))
  elif PNote3 != Note3.get('aria-label'):
   print ("Nouvelle note !") 
   print (Note3.get('aria-label'))
  elif PNote4 != Note4.get('aria-label'):
   print ("Nouvelle note !")
   print (Note4.get('aria-label'))
  else:  
   print ("Pas de nouvelles notes") 

 else:   # Sinon on enregistre et on print tout ça 
  d = shelve.open(bdn)
  d['ANote1'] = Note1.get('aria-label')
  d['ANote2'] = Note2.get('aria-label')
  d['ANote3'] = Note3.get('aria-label')
  d['ANote4'] = Note4.get('aria-label')
  d.close()
  print (" Les notes suivantes viennent d'être sauvegardées :")
  print ()
  print (Note1.get('aria-label'))
  print (Note2.get('aria-label'))
  print (Note3.get('aria-label'))
  print (Note4.get('aria-label'))
  print ()
 time.sleep(50)
