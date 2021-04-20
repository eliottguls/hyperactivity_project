from guizero import App, Picture, Text, PushButton, Box
from random import choice
import time

montemps = 0
OK = 0
Avant = 0
Apres = 0
stats = []
chat = 0
t_Avant, t_OK, t_Apres, t_stats = 0,0,0,0

def start():
    app.repeat(80,do_animation)

def do_animation():
    global montemps, chat, OK, Avant, Apres
    triee = []
    triee = stats.sort()
    if pict2.image=="cat.png":
        chat+=1
    if chat>=10:
        box.show()
        t_Avant = Text(box, text="Avant : %s" % Avant, grid=[1,0])
        t_OK = Text(box, text="OK : %s" % OK, grid=[1,1])
        t_Apres = Text(box, text="Apres : %s" % Apres, grid=[1,2])
        t_min = Text(box, text="Min : %s" % round(min(stats), 3), grid=[1,3])
        t_max = Text(box, text="Max : %s" % round(max(stats), 3), grid=[1,4])
        t_med = Text(box, text="Med : %s" % round(len(triee)/2, 3),width=100, height=100, grid=[1,5])
        #t_moy = Text(box, text="Moy : %s" % round((stats)+1/2), 3), grid=[0,6])
        stats.clear()
        OK, Avant, Apres, chat = 0,0,0,0
        app.cancel(do_animation)
    for u in reversed(range(1,5)):
        exec("pict%s.image = pict%s.image" %(u,u-1))
    pict0.image = choice(liste)
    montemps=time.time()

def do_event():
    global montemps, OK, Avant, Apres
    if pict2.image=="cat.png":
        OK += 1
        stats.append(time.time()-montemps)
        print("OK ---> ",time.time()-montemps)
    elif pict1.image=="cat.png":
        Avant += 1
        print("Avant")
    elif pict3.image=="cat.png":
        Apres += 1
        print("Apres")
        
liste=["velo.png","car.png","dog.png","cat.png","flower.png","flower.png","house.png","tree.png"]
app = App(title="hyper",layout="grid", width=530, height=500)
cadre = Picture(app, image = "Cadre ROUGE.png",width=110, height=110, grid=[2,1])

for i in range(5):
    exec("pict%s = Picture(app, image=liste[i],grid=[i,1])" % i)

start = PushButton(app, text=commencer)