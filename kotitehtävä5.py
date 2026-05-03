import tkinter as tk
import random
import math

#Ohjelmat ei toimi kaikki putkeen, kun määrittelin saman nimisiä aliohjelmia ja funktioita. 
#Varmaan on myös joku toinen syy, mutten keksi että mikä :D
# 2 ja/tai 3 tehtävät täytyy olla kokonaan kommenttina sillä aikaa, kun ajaa seuraavan tehtävän ohjelmia

# tehtävä 1



def piirra_kasvavasti(maksimi, r):
    root = tk.Tk()
    root.title("Kasvava pino")
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    x0 = 20
    y = 30
    vali_x = r * 2 + 20
    vali_y = r * 2 + 20

    for i in range(1, maksimi + 1):
        x = x0
        for k in range(i):
            canvas.create_oval(x, y, x + 2 * r, y + 2 * r, outline = "black")
            x = x + vali_x
        y = y + vali_y

    root.mainloop()

piirra_kasvavasti(7, 10)

#tehtävä 2
"""
def f(x):
    return 0.02 * (x - 150)**2 + 80

def paivita(root, canvas, x , dx, viive):
    r = 20
    x_min = 50
    x_max = 250

    while True:
        canvas.delete("all")

        y = f(x)
        x = x + dx
        
        canvas.create_oval(x - r, y - r, x + r, y + r, outline="black")

        if (x >= x_max):
            x = x_max
            dx = -dx

        if (x <= x_min):
            x = x_min
            dx = -dx

            
        root.update()
        root.after(viive)


def animaatio_paraabeli():
    root = tk.Tk()
    root.title("Pallo parabelilla")
    canvas1 = tk.Canvas(root, width=300, height=300, bg="white")
    canvas1.pack()

    x_aloitus = 150       
    dx = 1.5              
    viive = 10            

    paivita(root, canvas1, x_aloitus, dx, viive)
    root.mainloop()

animaatio_paraabeli()
"""
#tehtävä 3
"""
def f(x):
    return 0.02*x + 100

def paivita_pomppu(root, canvas, x , dx, r, viive):
    
    x_min = 50
    x_max = 250
    dr = 2

    while True:
        canvas.delete("all")

        y = f(x)
        x = x + dx
        r = r + dr
        canvas.create_oval(x - r, y - r, x + r, y + r, outline="black")

        if (x >= x_max):
            x = x_max
            dx = -dx
            dr = -dr

        if (x <= x_min):
            x = x_min
            dx = -dx
            dr = -dr
        
      
        root.update()
        root.after(viive)


def animaatio_pomppu():
    root = tk.Tk()
    root.title("Pomppupallo")
    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()
     
    x_aloitus = 150       
    dx = 1.5              
    viive = 10  
    r = 5 
              
              

    paivita_pomppu(root, canvas, x_aloitus, dx, r, viive)
    root.mainloop()

animaatio_pomppu()
"""

#tehtävä 4 

def piirra_ruudukko():
    root = tk.Tk()
    root.title("Ruudukko")
    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    koko = 300
    solu = 30

    for x in range(0, koko, solu):
        canvas.create_line(x, 0, x, koko)


    for y in range(0, koko, solu):
        canvas.create_line(0, y, koko, y)

    root.mainloop()

piirra_ruudukko()

#tehtävä 5

def piirra_varillinen_ruudukko(canvas, leveys, korkeus, vari_lista, solu=30):

    i = 0

    for y in range(korkeus):
        for x in range(leveys):

            x1 = x * solu
            y1 = y * solu
            x2 = x1 + solu
            y2 = y1 + solu

            if vari_lista[i]:
                vari = "black"
            else:
                vari = "white"

            canvas.create_rectangle(x1, y1, x2, y2, fill=vari, outline="black")

            i = i + 1


def varit():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    leveys = 10
    korkeus = 10


    lista = [
    True, False, True, False, True, False, True, False, True, False,
    False, True, False, True, False, True, False, True, False, True,
    True, False, True, False, True, False, True, False, True, False,
    False, True, False, True, False, True, False, True, False, True,
    True, False, True, False, True, False, True, False, True, False,
    False, True, False, True, False, True, False, True, False, True,
    True, False, True, False, True, False, True, False, True, False,
    False, True, False, True, False, True, False, True, False, True,
    True, False, True, False, True, False, True, False, True, False,
    False, True, False, True, False, True, False, True, False, True,
    ]

    piirra_varillinen_ruudukko(canvas, leveys, korkeus, lista)

    root.mainloop()
varit()
