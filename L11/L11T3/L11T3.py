######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:25.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#L12T1

#aliohjelma

def tulostus(sana, n,m):

    if n != m:
        print("Sana on '{0}', {1}. kerta.".format(sana,m))
        tulostus(sana,n,m+1)
    else:
        print("Sana on '{0}', {1}. kerta.".format(sana,m))
    return None

#paaohjelma
def paaohjelma():
    sana = input("Anna tulostettava sana: ")
    kerrat = int(input("Anna tulostuskertojen määrä: "))
    tulostus(sana,kerrat,1)
    print("Kiitos ohjelman käytöstä.")
    return


paaohjelma()