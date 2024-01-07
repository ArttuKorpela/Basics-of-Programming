######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:03.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
# https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
#L12T2
import math
def muunnos(luku):
    loppu = 0
    kaannos = luku[::-1]

    for i in range(len(kaannos)):
        loppu += int(kaannos[i])*math.pow(2,i)
    return int(loppu)



num1 = input("Anna ensimmäinen binaariluku: ")
num2 = input("Anna toinen binaariluku: ")

m1 = muunnos(num1)
m2 = muunnos(num2)
print("Bittijonosi {0} on kymmenkantaisena kokonaislukuna {1}".format(num1,m1))
print("Bittijonosi {0} on kymmenkantaisena kokonaislukuna {1}".format(num2,m2))
print("Lukujen {0} ja {1} erotus on {2}".format(m1,m2,m1-m2))
print("Kiitos ohjelman käytöstä.")