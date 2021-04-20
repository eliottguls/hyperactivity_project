"""
Auteur: Eliott GUILLOSSOU
Descriptif :Ce programme peut être utilisé pour détecter une hyperactivité eventuelle chez l'utilisateur.
En effet, des images défileront sur votre écran et lorsque le chien sera dasn le cadre rouge il faudra
appuyer sur la barre espace.Le nombre de fois où l utilisateur appuie avant, après et correct seront enregistrées
et analyser par un neurologue. Une moyenne et une médiane seront également calculés puis analysés.
"""


from guizero import App, Picture, Text, PushButton,Box
from random import* 
import time
liste=["img/flower.png","img/bicycle.png","img/car.png","img/cat.png","img/dog.png","img/house.png","img/tree.png"]



'''mise en place d'un chronomètre '''
cpt=0
chrono=0
def time():
        global chrono,cpt
        cpt=cpt+1
        text_moy.value = str(cpt)
        if cpt>25:
            print("Fin")
            app.cancel(do_animation)
    



'''arrêt du défilement des images'''
def stop():
    app.cancel(do_animation)



'''redémarrage du défilement des images si arrêt au préalable'''
def start():
    app.cancel(do_animation)
    app.repeat(500,do_animation)
    
    

'''défilement des images aléatoirement choisi '''
def do_animation():
            pict5.image = pict4.image
            pict4.image = pict3.image
            pict3.image = pict2.image
            pict2.image = pict1.image
            pict1.image = choice(liste)



'''choix de l'affice de l'interface graphique'''
app = App(title="hyper",layout="grid")

'''mise en place des boutons'''    
Button = PushButton(app, command=start,grid=[1,4],text="Start")
Button = PushButton(app, command=stop,grid=[3,4],text="Stop")

'''Importation des images'''
pict1 = Picture(app, image="img/White.png",width=100, height=100,grid=[0,1])
pict2 = Picture(app, image="img/White.png",width=100, height=100,grid=[1,1])
cadre = Picture(app, image="img/Cadre_ROUGE.png",width=110, height=110,grid=[2,1])
pict3 = Picture(app, image="img/White.png",width=100, height=100,grid=[2,1])
pict4 = Picture(app, image="img/White.png",width=100, height=100,grid=[3,1])
pict5 = Picture(app, image="img/White.png",width=100, height=100,grid=[4,1])
message = Text(app, text="Image cyclique",grid=[2,0])
    
'''création d'un espace d'affichage pour les données calculées'''
buttons_box = Box(app, width="fill", align="bottom", border=True)
text_moy = Text(buttons_box, text=chrono)

'''Création graphique des boutons "Start","Stop"'''
Button = PushButton(app, command=start,grid=[1,4],text="Start")
Button = PushButton(app, command=stop,grid=[3,4],text="Stop")


app.repeat(500,do_animation)
app.display()