"""
Auteur: Eliott GUILLOSSOU
Descriptif :Ce programme peut être utilisé pour détecter une hyperactivité eventuelle chez l'utilisateur.
En effet, des images défileront sur l'écran et lorsque le chien sera dans le cadre rouge il faudra
appuyer sur la barre espace.Le nombre de fois où l utilisateur appuie avant, après et au bon moment seront enregistrées
et analyser par un neurologue. Une moyenne et une médiane seront également calculés puis analysés. Il faudra en premier temps
construire les fonctions qui permettront d'obtenir les résultats en fonction des temps relevés lors du test 
"""


from guizero import App, Picture, Text, PushButton, Box, TextBox
from random import choice
import time

''' Définition,création des variables'''
chrono = 0
OK = 0
Avant = 0
Apres = 0
stats = []
duree = 0
temps_debut = 0
statutLoop = 0
oneTouch = 0

''' Fonction qui retourne le minimum d'une liste'''
def mini(lst):
    if not(lst):
        return 0
    minimum = lst[0]
    for i in lst:
        if i <= minimum:
            minimum = i
    return round(minimum, 3)

''' Fonction qui retourne le maximum d'une liste'''
def maxi(lst):
    if not(lst):
        return 0
    maximum = lst[0]
    for i in lst:
        if i >= maximum:
            maximum = i
    return round(maximum, 3)

''' Fonction qui retourne la mediane d'une liste'''
def med(lst):
    lst = sorted(lst)
    n = len(lst)
    if not(lst):
        return 0
    if n < 1:
        return None
    if n % 2 == 0 :
        return round((lst[n//2-1] + lst[n//2] ) / 2, 3)
    else:
        return round(lst[n//2], 3)

''' Fonction qui retourne la moyenne d'une liste'''
def moyenne(lst):
    somme = 0
    if not(lst):
        return 0
    for val in lst:
        somme += val
    return round(somme/len(lst), 3)

'''Définition du bouton start'''
def start():
    global duree, temps_debut, statutLoop
    duree = int(temps_exec.value)
    temps_exec.clear()
    temps_debut = time.time()
    app.repeat(200,do_animation)
    statutLoop = True

''' Créer l'animation '''
def do_animation():
    global chrono, OK, Avant, Apres, duree, temps_debut, statutLoop, oneTouch
    chrono=time.time()
    oneTouch = True
    
    # Si jamais le temps est equivalent au temps fixé par l'utilisateur,
    # le programme s'arrête et execute le programme ci dessous
    if (chrono-temps_debut)>=duree:
        box.show()
        statutLoop = False
        t_Avant = Text(box, text="Avant : %s" % Avant, grid=[0,0])
        t_OK = Text(box, text="OK : %s" % OK, grid=[0,1])
        t_Apres = Text(box, text="Apres : %s" % Apres, grid=[0,2])
        t_min = Text(box, text="Minimum : %s" % mini(stats), grid=[0,3])
        t_max = Text(box, text="Maximum : %s" % maxi(stats), grid=[0,4])
        t_med = Text(box, text="Mediane : %s" % med(stats), grid=[0,5])
        t_moy = Text(box, text="Moyenne : %s" % moyenne(stats), grid=[0,6])
        stats.clear()
        OK, Avant, Apres = 0,0,0
        app.cancel(do_animation)
        
    ''' Cycle des images'''
    pict4.image = pict3.image
    pict3.image = pict2.image
    pict2.image = pict1.image
    pict1.image = pict0.image
    pict0.image = choice(liste)
    while pict0.image == pict1.image:
        pict0.image = choice(liste)

'''S'execute quand une touche du clavier est présée'''
def event_Clavier():
    global chrono, OK, Avant, Apres, statutLoop, oneTouch
    if statutLoop and oneTouch: # Les entrées clavier ne s'execute que quand la boucle tourne et évite plusieurs entrées par image (pour éviter le fait que l'on puisse appuyer deux fois en une seule image et donc un élement en trop dans notre liste)
        if pict2.image=="img/dog.png":
            OK += 1
            stats.append(time.time()-chrono)
        elif pict1.image=="img/dog.png":
            Avant += 1
        elif pict3.image=="img/dog.png":
            Apres += 1
        oneTouch = False

'''Création de la liste contenant toutes les images'''
liste=["img/bicycle.png","img/car.png","img/dog.png","img/cat.png","img/flower.png","img/house.png","img/tree.png"]

app = App(title="hyper",layout="grid", width=530, height=500) # Création de l'application

cadre = Picture(app, image = "img/cadre_rouge.png",width=110,height=110,grid=[2,1]) # Création du cadre rouge

'''Création de cadres et importation des premières images'''
pict0 = Picture(app, image="img/bicycle.png",grid=[0,1])
pict1 = Picture(app, image="img/car.png",grid=[1,1])
pict2 = Picture(app, image="img/cat.png",grid=[2,1])
pict3 = Picture(app, image="img/dog.png",grid=[3,1])
pict4 = Picture(app, image="img/flower.png",grid=[4,1])

'''Création des widgets (boutons, barre de saisie, boites...)'''
start = PushButton(app, text='Start', command=start, grid=[2,2])
box = Box(app, layout="grid", grid=[2,3])
temps_exec = TextBox(app,text="Durée(sc)", grid=[1,2])

app.when_key_pressed = event_Clavier #Gestion des évenements clavier
app.display() #Affichage de l'application