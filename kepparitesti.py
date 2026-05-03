from keppihevonen import Keppihevonen
from kepparitalli import Kepparitalli



def testaa_hevosia():
    k1 = Keppihevonen("Jaska", 0.75, True)
    k2 = Keppihevonen("Tumppi", 0.9, False)

    k1_ulkonäkö = k1.merkkijonomuodossa()
    print(k1_ulkonäkö)

    k2_un = k2.merkkijonomuodossa()
    print(k2_un)

    k1.kasva_sentti()
    print(k1.merkkijonomuodossa())
    print(k2.merkkijonomuodossa())
  
    print()
    print(k1.merkkijonomuodossa())
    print(k2.merkkijonomuodossa())

    print("here: ")
    print(k1)


def testaa_tallia():
    print("Tallitesti alkaa: ")
    k1 = Keppihevonen("Jaska", 0.75, True)
    k2 = Keppihevonen("Tumppi", 0.9, False)
    k3 = Keppihevonen("Ansku", 0.67, False)
    k4 = Keppihevonen("Jansku", 0.67, False)


    t1 = Kepparitalli("Turku A-ryhmä", 46)
    t1.lisää(k1)
    t1.lisää(k2)
    t1.lisää(k3)
    t1.lisää(k4)
    t1.lisää(k1)
    t1.elämöi()


#testaa tehtävät 2 ja 3
def testaa_hevosen_tiedosto():
    k1 = Keppihevonen("Jaska", 0.75, True)
    k2 = Keppihevonen("Tumppi", 0.9, False)

    avattu_tied = open("hevoset.txt", "w", encoding="utf-8")
    k1.tallenna_tiedostoon(avattu_tied)
    k2.tallenna_tiedostoon(avattu_tied)
    avattu_tied.close()

    avattu_tied = open("hevoset.txt", "r", encoding="utf-8")
    uusi1 = Keppihevonen.lue_tiedostosta(avattu_tied)
    uusi2 = Keppihevonen.lue_tiedostosta(avattu_tied)
    avattu_tied.close()

    print(uusi1)
    print(uusi2)


#testaa tehtävät 4 ja 5
def testaa_tallin_tiedosto():
    k1 = Keppihevonen("Jaska", 0.75, True)
    k2 = Keppihevonen("Tumppi", 0.9, False)
    k3 = Keppihevonen("Ansku", 0.67, False)
    k4 = Keppihevonen("Jansku", 0.67, False)

    t1 = Kepparitalli("Turku A-ryhmä", 46)
    t1.lisää(k1)
    t1.lisää(k2)
    t1.lisää(k3)
    t1.lisää(k4)

    t1.tallenna_tiedostoon("talli.txt")

    uusi_talli = Kepparitalli.lue_tiedostosta("talli.txt")
    uusi_talli.elämöi()


testaa_hevosia()
testaa_tallia()
testaa_hevosen_tiedosto()
testaa_tallin_tiedosto()