import tkinter as tk
import random
import math

#5

def piirra_vari_ruudukko(leveys, korkeus, lista):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=leveys*30, height=korkeus*30)
    canvas.pack()

    i = 0
    for y in range(korkeus):
        for x in range(leveys):
            x1 = x*30
            y1 = y*30
            x2 = x1 + 30
            y2 = y1 + 30
            vari = "black" if lista[i] else "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=vari, outline="black")
            i += 1

    root.mainloop()

piirra_vari_ruudukko(5, 5, [
    True, False, True, False, True,
    False, True, False, True, False,
    True, False, True, False, True,
    False, True, False, True, False,
    True, False, True, False, True
])