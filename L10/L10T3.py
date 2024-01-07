######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:20.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#L10T3
import numpy
sarakkeet = 4
rivit = 4

print("Tämä ohjelma testaa numpy-matriisin käyttöä.\n"
      "Matriisi tulostettuna numpy-muotoilulla:")
matriisi = numpy.zeros((rivit,sarakkeet),int)

for rivi in range(rivit):
    for sarake in range(sarakkeet):
        matriisi[rivi][sarake] = (rivi+1)*(sarake+1)
print(matriisi)
print()
print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
for rivi in range(rivit):
    for sarake in range(sarakkeet):
        print(matriisi[rivi][sarake],end=";")
    print()
print()
print("Kiitos ohjelman käytöstä.")
