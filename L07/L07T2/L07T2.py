######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:22.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#Luokat
class TILI:
    Nimi=""
    Saldo=0



#aliohjelma
def kysely(olio):
    olio.Nimi=input("Anna pankkitilin nimi: ")
    olio.Saldo=float(input("Anna pankkitilin saldo: "))
    return olio
def tulostus(olio):
    print("Pankkitilillä '{0}' on nyt rahaa {1}e.".format(olio.Nimi,round(olio.Saldo,2)))

#paaohjelma

def paaohjelma():
    pankkitili=TILI()
    pankkitili=kysely(pankkitili)
    tulostus(pankkitili)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
# Tehtävä L07T2.py
# EOF