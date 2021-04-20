from guizero import App, Picture
from random import* 

liste=["flower.png","bicycle.png","car.png","cat.png","dog.png","house.png","tree.png"]


def do_animation():
    pict5.image = pict4.image
    pict4.image = pict3.image
    pict3.image = pict2.image
    pict2.image = pict1.image
    pict1.image = choice(liste)

app = App(title="hyper",layout="grid")


pict1 = Picture(app, image="white.png",width=100, height=100,grid=[1,3])
pict2 = Picture(app, image="white.png",width=100, height=100,grid=[2,3])
pict3 = Picture(app, image="Cadre ROUGE.png",width=110, height=110,grid=[3,3])
pict3 = Picture(app, image="white.png",width=100, height=100,grid=[3,3])
pict4 = Picture(app, image="white.png",width=100, height=100,grid=[4,3])
pict5 = Picture(app, image="white.png",width=100, height=100,grid=[5,3])

app.repeat(randint(1000,5000),do_animation)

app.display()