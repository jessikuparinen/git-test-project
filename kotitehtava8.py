#1
inventory = {
    "potato": 15,
    "apple": 10,
    "kiwi": 13,
    "turnip": 7
}

price = {
    "potato": 1,
    "apple": 2,
    "kiwi": 1.5,
    "turnip": 0.5
}

inventory["potato"] += 10
inventory["pear"] = 5
price["pear"] = 1.5

print(inventory)
print(price)

def korota_hintoja(price):
    for tuote in price:
        price[tuote] = price[tuote] * 1.1

korota_hintoja(price)
print(price)

def laske_kokonaisarvo(inventory, price):
    summa = 0

    for tuote in inventory:
        summa += inventory[tuote] * price[tuote]

    return summa

arvo = laske_kokonaisarvo(inventory, price)
print(arvo)

#2
def convert_dict(d):
    uusi = {}

    for avain in d:
        arvo = d[avain]
        uusi[arvo] = avain

    d.clear()
    d.update(uusi)

example = {
    100: "velocity",
    101: "humidity",
    102: "SNR",
    103: "RSSI"
}

convert_dict(example)
print(example)

#3
def eniten_nested(lista):
    max_lkm = 0
    yleisin = ""

    for i in lista:
        laskuri = 0

        for j in lista:
            if i == j:
                laskuri += 1

        if laskuri > max_lkm:
            max_lkm = laskuri
            yleisin = i

    return yleisin, max_lkm

def eniten_dict(lista):
    laskuri = {}

    for sana in lista:
        if sana in laskuri:
            laskuri[sana] += 1
        else:
            laskuri[sana] = 1

    max_lkm = 0
    yleisin = ""

    for sana in laskuri:
        if laskuri[sana] > max_lkm:
            max_lkm = laskuri[sana]
            yleisin = sana

    return yleisin, max_lkm

data = ["aaaa", "bbbb", "aaaa", "cccc", "cccc", "bbbb", "cccc"]

tulos1 = eniten_nested(data)
tulos2 = eniten_dict(data)

print("Nested:", tulos1[0], "appeared", tulos1[1], "times")
print("Dict:", tulos2[0], "appeared", tulos2[1], "times")

#Sisäkkäiset silmukat ovat hitaita isoilla listoilla, koska ne käyvät listan
# monta kertaa läpi. Dict on nopeampi koska lista käydään läpi vain kerran

#4
import random
suits = ["clubs", "diamonds", "hearts", "spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [(s, v) for s in suits for v in values]

print("Kortteja pakassa: ", len(deck))

deck[1] = ("spades", "3")
print("Toinen kortti vaihdon jälkeen: ", deck[1])

random.shuffle(deck)
print("Sekoitettu pakka: ")
print(deck)

kortti = random.choice(deck)
print("Satunnainen kortti:", kortti[0], kortti[1])

pelaaja1 = []
pelaaja2 = []
pelaaja3 = []
pelaaja4 = []

for i in range(len(deck)):
    if i % 4 == 0:
        pelaaja1.append(deck[i])
    elif i % 4 == 1:
        pelaaja2.append(deck[i])
    elif i % 4 == 2:
        pelaaja3.append(deck[i])
    else:
        pelaaja4.append(deck[i])

print("Pelaaja 1: ", pelaaja1)
print("Pelaaja 2: ", pelaaja2)
print("Pelaaja 3: ", pelaaja3)
print("Pelaaja 4: ", pelaaja4)

#Pakassa voi olla sama kortti kahdesti koska vain yksi kortti korvattiin
#eikä alkuperäistä poistettu

#5
suits = ["clubs", "diamonds", "hearts", "spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [(s, v) for s in suits for v in values]

random.shuffle(deck)

kate = []
for i in range(5):
    kate.append(deck[i])

print("Käsi: ", kate)

def arvo_numeroon(arvo):
    if arvo == "J": return 11
    if arvo == "Q": return 12
    if arvo == "K": return 13
    if arvo == "A": return 14
    return int(arvo)

numerot = []
for kortti in kate:
    numerot.append(arvo_numeroon(kortti[1]))

numerot.sort()

on_suora = True
for i in range(4):
    if numerot[i] + 1 != numerot[i+1]:
        on_suora = False

if on_suora:
    print("Suora")
else:
    print("Ei suoraa")