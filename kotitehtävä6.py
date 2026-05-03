#1

class Klapi:
    def __init__(self, puulaji, massa):
        self.puulaji = puulaji
        self.massa = massa
        self.palaa = False

    def sytyta(self):
        self.palaa = True

    def sammuta(self):
        self.palaa = False

    def pala(self, maara):
        if self.palaa:
            self.massa -= maara
            if self.massa < 0:
                self.massa = 0

        else:
            print("Klapi ei pala, joten massa ei vähene.")

    def __str__(self):
        tila = "palaa" if self.palaa else "ei pala"
        return f"Klapi: puulaji = {self.puulaji}, massa = {self.massa}, tila = {tila}"
    
#2

class Tulipesa:
        def __init__(self):
            self.klapit = []

        def lisaa_klapi(self, klapi):
            self.klapit.append(klapi)

        def sytyta_kaikki(self):
            for klapi in self.klapit:
                klapi.sytyta()

        def polta(self, maara):
            for klapi in self.klapit:
                klapi.pala(maara)

        def palamaton_massa(self):
            summa = 0
            for klapi in self.klapit:
                if not klapi.palaa:
                    summa += klapi.massa
            return summa
        
        def __str__(self):
            teksti = "Tulipesä:\n"
            for i, klapi in enumerate(self.klapit, start=1):
                teksti += f" {i}. {klapi}\n"
            teksti += f"Palamaton massa yhteensä: {self.palamaton_massa()}"
            return teksti

#3a

# index() Palauttaa merkkijonosta ensimmäisen
# annetun merkkijonon indeksin, tai virheen
# jos merkkijonoa ei löydy.

# count() Laskee, kuinka monta kertaa annettu 
# alimerkkijono esiintyy merkkijonossa.

# split() Jakaa merkkijonon osiin annetun erotinmerkin
# kohdalta

# title() Muuttaa merkkijonon jokaisen sanan ensimmäisen
# kirjaimen isoksi.

# lower() Muuttaa merkkijonon kaikki kirjaimet pieniksi.

# isnumeric() Tarkistaa, onko merkkijono kokonaan numeroita.

# 7 Muuta metodia

# upper() Muuttaa merkkijonon kaikki kirjaimet isoiksi.

# strip() Poistaa merkkijonon alusta ja lopusta välilyönnit.

# replace() Korvaa merkkijonossa kaikki esiintymät
# toisella merkkijonolla.

# find() Palauttaa merkkijonosta ensimmäisen indeksin
# tai -1 jos sitä ei löydy.

# startswith() Tarkistaa, alkaako merkkijono annetulla
# merkkijonolla.

# endswith() Tarkistaa, päättyykö merkkijono annetulla
# merkkijonolla.

# isalpha() Tarkistaa, onko merkkijono kokonaan kirjaimia. 

#3b

# append() Lisää alkion listan loppuun.

# remove() Poistaa listasta ensimmäisen annetun
# arvon esiintymän.

# clear() Poistaa kaikki alkiot listasta.

# reverse() Kääntää listan alkiot päinvastaiseksi.

# copy() Luo listasta kopion.

# sort() Järjestää listan alkiot nousevaan järjestykseen.

# count() Laskee, kuinka monta kertaa annettu arvo 
# esiintyy listassa.


print("LIUKULUVUT")
luvut = [3.2, 1.5, 3.2, 0.7]
print("Alku:", luvut)

luvut.append(4.0)
print("append:", luvut)

luvut.remove(1.5)
print("remove:", luvut)

print("count(3.2):", luvut.count(3.2))

luvut.sort()
print("sort:", luvut)

luvut.reverse()
print("reverse:", luvut)

kopio = luvut.copy()
print("copy:", kopio)

luvut.clear()
print("clear:", luvut)



print("MERKKIJONOT")
sanat = ["koira", "kissa", "koira", "hevonen"]
print("Alku:", sanat)

sanat.append("lammas")
print("append:", sanat)

sanat.remove("kissa")
print("remove:", sanat)

print("count('koira'):", sanat.count("koira"))

sanat.sort()
print("sort:", sanat)

sanat.reverse()
print("reverse:", sanat)

kopio = sanat.copy()
print("copy:", kopio)

sanat.clear()
print("clear:", sanat)

#4

import random

nollat = [0] * 10000
print("Nollalista (5 ekaa):", nollat[:5])
print("Pituus:", len(nollat))

print()

luvut = [random.uniform(-5, 5) for _ in range(10000)]
print("Satunnaiset (5 ekaa):", luvut[:5])

luvut.sort()
print("Järjestetty (5 pienintä):", luvut[:5])
print("Järjestetty (5 suurinta):", luvut[-5:])

print()

random.shuffle(luvut)
print("Sekoitettu (5 ekaa):", luvut[:5])

luvut.sort()
print("Uudelleen järjestetty (5 pienintä):", luvut[:5])
print("Uudelleen järjestetty (5 suurinta):", luvut[-5:])

#5

import tkinter as tk

LEVEYS = 600
KORKEUS = 400
MAARA = 20
SADE = 20

varit_vaihtoehdot = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]

x_koordinaatit = []
y_koordinaatit = []
varit = []

for i in range(MAARA):
    x = random.randint(SADE, LEVEYS - SADE)
    y = random.randint(SADE, KORKEUS - SADE)
    vari = random.choice(varit_vaihtoehdot)

    x_koordinaatit.append(x)
    y_koordinaatit.append(y)
    varit.append(vari)

ikkuna = tk.Tk()
ikkuna.title("Satunnaiset ympyrät")
canvas = tk.Canvas(ikkuna, width=LEVEYS, height=KORKEUS, bg="white")
canvas.pack()

for i in range(MAARA):
    x = x_koordinaatit[i]
    y = y_koordinaatit[i]
    vari = varit[i]

    canvas.create_oval(x - SADE, y - SADE, x + SADE, y + SADE, fill=vari)

ikkuna.mainloop()
    
#6

LEVEYS = 600
KORKEUS = 400
MAARA = 15

varit_vaihtoehdot = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]

x_koordinaatit = []
y_koordinaatit = []
varit = []

for i in range(MAARA):
    x = random.randint(0, LEVEYS)
    y = random.randint(0, KORKEUS)
    vari = random.choice(varit_vaihtoehdot)

    x_koordinaatit.append(x)
    y_koordinaatit.append(y)
    varit.append(vari)

ikkuna = tk.Tk()
ikkuna.title("Viivapiirrospolku")

canvas = tk.Canvas(ikkuna, width=LEVEYS, height=KORKEUS, bg="white")
canvas.pack()

for i in range(MAARA - 1):
    x1 = x_koordinaatit[i]
    y1 = y_koordinaatit[i]
    x2 = x_koordinaatit[i + 1]
    y2 = y_koordinaatit[i + 1]
    vari = varit[i]

    canvas.create_line(x1, y1, x2, y2, fill=vari, width=2)

ikkuna.mainloop()