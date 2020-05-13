#Pronote Push Service 1.0
# Developpe par Nico Isapro, Interface graphique par firelop_video
# Interface Graphique et dos pour python 3
# Lire le fichier readme

import sys
import os
import time
import dryscrape 
import shelve
import getpass
import bs4
import PySimpleGUI as sg
import winsound #Module par défaut de python pour les sons


         
sg.popup("Pronote Push Service V1.0 - Lycée Louis Vincent", "Nico Isapro")
 # PARTIE IDENTIFIANTS ETC 

bdd = "login.dat"
bdn = "notes.dat"

if os.path.isfile(bdd): # Si fichier présent
 d = shelve.open(bdd)
 username = d['username']
 password = d['password']
 pronote_url = d['pronote_url']
 sg.popup("Pronote Push Service V1.0 - Lycée Louis Vincent", "Compte enregistré : " + username)
 print ()
 d.close()

else:    # Sinon, on demande les identifiants 
 username = sg.popup_get_text("Pronote Push Service V1.0 - Lycée Louis Vincent", "Nom d'utilisateur : ")
 password = sg.popup_get_text("Pronote Push Service V1.0 - Lycée Louis Vincent", "Mot de passe : ", password_char="*")
 pronote_url = sg.popup_get_text("Pronote Push Service V1.0 - Lycée Louis Vincent", "Url de pronote pour votre établisement : ")

# On sauvegarde tout ça 
 d = shelve.open(bdd)
 d['username'] = username
 d['password'] = password
 d['pronote_url'] = pronote_url
 d.close()
 sg.popup("Pronote Push Service V1.0 - Lycée Louis Vincent", "Compte créé avec succès !")
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
 sess.visit(pronote_url)
 time.sleep(4)  # Ne pas modifier cette ligne


# PARSING #
 soup = bs4.BeautifulSoup(sess.body(), "lxml")
 Note1 = soup.find('div', id="GInterface.Instances[1]_notes_0")  
 Note2 = soup.find('div', id="GInterface.Instances[1]_notes_1")  #SUPPRIMER CETTE LIGNE SI VOUS N'AVEZ PAS ENCORE 2 NOTES !
 Note3 = soup.find('div', id="GInterface.Instances[1]_notes_2")  #SUPPRIMER CETTE LIGNE SI VOUS N'AVEZ PAS ENCORE 3 NOTES !
 Note4 = soup.find('div', id="GInterface.Instances[1]_notes_3")  #SUPPRIMER CETTE LIGNE SI VOUS N'AVEZ PAS ENCORE 4 NOTES !


# PARTIE TRAITEMENT #
 if os.path.isfile(bdn): # Si fichier présent on compare les notes
  d = shelve.open(bdn)
  PNote1 = d['ANote1']
  PNote2 = d['ANote2']
  PNote3 = d['ANote3']
  PNote4 = d['ANote4']
  d.close()
  if PNote1 != Note1.get('aria-label'):   # A OPTIMISER...
   sg.SystemTray.notify('Nouvelle note !', Note1.get('aria-label'))
   winsound.PlaySound("notif.wav", winsound.SND_NOWAIT)
   
  elif PNote2 != Note2.get('aria-label'):
   sg.SystemTray.notify('Nouvelle note !', Note2.get('aria-label'))
   winsound.PlaySound("notif.wav", winsound.SND_NOWAIT)
   
  elif PNote3 != Note3.get('aria-label'):
   sg.SystemTray.notify('Nouvelle note !', Note3.get('aria-label'))
   winsound.PlaySound("notif.wav", winsound.SND_NOWAIT)
   
  elif PNote4 != Note4.get('aria-label'):
   sg.SystemTray.notify('Nouvelle note !', Note4.get('aria-label'))
   winsound.PlaySound("notif.wav", winsound.SND_NOWAIT)

 else:   # Sinon on enregistre et on print tout ça 
  d = shelve.open(bdn)
  d['ANote1'] = Note1.get('aria-label')
  d['ANote2'] = Note2.get('aria-label')
  d['ANote3'] = Note3.get('aria-label')
  d['ANote4'] = Note4.get('aria-label')
  d.close()
  
  sg.popup ("Les notes suivantes viennent d'être sauvegardées : \n{}\n{}\n{}\n{}".format(Note1.get('aria-label'), Note2.get('aria-label'), Note3.get('aria-label'), Note4.get('aria-label')))


 time.sleep(50)
