from keppihevonen import Keppihevonen


class Kepparitalli:

    def __init__(self, tallin_nimi, kepparimaksimi):
        """Alustaa uuden tallin tyhjäksi ja lailliseen tilaan."""
        self.__nimi = tallin_nimi
        self.__paikkojen_max_lkm = kepparimaksimi
        self.__kepparit = []

 
    def tallissa_tilaa(self):
        """Onko tallissa tilaa?"""
        return len(self.__kepparit) < self.__paikkojen_max_lkm


    def lisää(self, keppari):
        """Lisää kepparin talliin, kun tilaa on.
        Alkuehto: self.tallissa_tilaa() """
       
        assert self.tallissa_tilaa(), "Tallissa ei ole tarpeeksi tilaa." 
        self.__kepparit.append(keppari)


    def elämöi(self):
        """Tulostaa tallin nykyhetken elämöinnin ruudulle."""
        for hepo in self.__kepparit:
            print(hepo)


    #4
    def tallenna_tiedostoon(self, tiedoston_nimi):
        avattu_tied = open(tiedoston_nimi, "w", encoding="utf-8")

        avattu_tied.write(self.__nimi + ";" +
                          str(self.__paikkojen_max_lkm) + ";" +
                          str(len(self.__kepparit)) + "\n")

        for keppari in self.__kepparit:
            keppari.tallenna_tiedostoon(avattu_tied)

        avattu_tied.close()


    #5
    @staticmethod
    def lue_tiedostosta(tiedoston_nimi):
        avattu_tied = open(tiedoston_nimi, "r", encoding="utf-8")

        eka_rivi = avattu_tied.readline().strip()
        osat = eka_rivi.split(";")

        tallin_nimi = osat[0]
        kepparimaksimi = int(osat[1])
        kepparien_lkm = int(osat[2])

        uusi_talli = Kepparitalli(tallin_nimi, kepparimaksimi)

        for _ in range(kepparien_lkm):
            uusi_keppari = Keppihevonen.lue_tiedostosta(avattu_tied)
            if uusi_keppari is not None:
                uusi_talli.lisää(uusi_keppari)

        avattu_tied.close()
        return uusi_talli