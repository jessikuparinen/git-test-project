#1
#Tutustuin itsissä oleviin koodeihin ja tarkastelin niitä.
#Testasin keppihevosten luontia, tulostamista ja pituuden kasvattamista
# ja kokeilin muutaa lukuja tms jotta näkisin mitä ne tekevät. 

#2
class Keppihevonen:

    def __init__(self, uusi_nimi, uusi_pituus, onKovapäinen):
        self.__nimi = uusi_nimi
        self.__pituus = uusi_pituus
        self.__onKova = onKovapäinen

 
    def __str__(self):
        return self.merkkijonomuodossa()


    def merkkijonomuodossa(self):
        palautettava = ""
        palautettava += self.__nimi
        palautettava += ": "
        palautettava += str(self.__pituus)

        if (self.__onKova):
            pää = "[]____ "
        else:
            pää = "()____ "

        palautettava = pää + palautettava
        return palautettava


    def kasva_sentti(self):
        self.__pituus = self.__pituus + 0.01


    def tallenna_tiedostoon(self, avattu_tied):
        assert not avattu_tied.closed
        assert avattu_tied.writable()

        rivi = self.__nimi + ";" + str(self.__pituus) + ";" + str(self.__onKova) + "\n"
        avattu_tied.write(rivi)


def testaa():
    print("Testi alkaa")

    k1 = Keppihevonen("Jaska", 0.75, True)
    k2 = Keppihevonen("Tumppi", 0.9, False)

    print(k1)
    print(k2)

    tiedosto = open("hevoset.txt", "w")

    k1.tallenna_tiedostoon(tiedosto)
    k2.tallenna_tiedostoon(tiedosto)

    tiedosto.close()

    print("Tallennettu tiedostoon!")


testaa()

#3

@staticmethod
def lue_tiedostosta(avattu_tied):
     assert not avattu_tied.closed
     assert avattu_tied.readable()

    rivi = avattu_tied.readline()

    if rivi == "":
        return None

    rivi = rivi.strip()
    osat = rivi.split(";")

    nimi = osat[0]
    pituus = float(osat[1])
    on_kova = (osat[2] == "True")

    return Keppihevonen(nimi, pituus, on_kova)