class Keppihevonen:

    def __init__(self, uusi_nimi, uusi_pituus, onKovapäinen):
        """Alustaa uuden keppihevosen, jonka nimeksi tulee uusi_nimi,
           pituudeksi uusi_pituus (metreinä) ja pään kovuus määräytyy
           onKovapäinen-bool argumentin mukaan."""
        self.__nimi = uusi_nimi
        self.__pituus = uusi_pituus
        self.__onKova = onKovapäinen

 
    def __str__(self):
        """Palauttaa olion esityksen merkkijonomuodossa."""
        return self.merkkijonomuodossa()


    def merkkijonomuodossa(self):
        """Palauttaa olion esityksen merkkijonomuodossa."""
        palautettava = ""
        palautettava += self.__nimi
        palautettava += ": "
        palautettava += str(self.__pituus)

        if self.__onKova:
            pää = "[]____ "
        else:
            pää = "()____ "

        palautettava = pää + palautettava
        return palautettava


    def kasva_sentti(self):
        """Kasvattaa keppihevosen kokoa yhden senttimetrin."""
        self.__pituus = self.__pituus + 0.01


    #2
    def tallenna_tiedostoon(self, avattu_tied):
        """Tallentaa yhden keppihevosen tiedot yhdelle riville."""
        assert not avattu_tied.closed
        assert avattu_tied.writable()

        rivi = self.__nimi + ";" + str(self.__pituus) + ";" + str(self.__onKova) + "\n"
        avattu_tied.write(rivi)
    


    #3
    @staticmethod
    def lue_tiedostosta(avattu_tied):
        """Lukee yhden keppihevosen tiedot tiedostosta ja palauttaa uuden olion."""
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
    
