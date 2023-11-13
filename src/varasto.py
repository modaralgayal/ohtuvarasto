"""Exporting this to main"""

class Varasto:

    """ Varasto sisältää kaikki toiminnot sekä antaa kaikki arvot varastointiin liittyen """

    def __init__(self, tilavuus, alku_saldo = 0):

        """ Initiating values """

        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        """ Tells how much space is left """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """ Adding functionality """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """ Functionality for taking from the storage """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """ Return value """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
