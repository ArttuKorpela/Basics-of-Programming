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
#L11T2

kuukausi = int(input("Anna kuukausien lukumäärä: "))


n = None

lista = [1]

for i in range(kuukausi):
    m = i+1
    if m == 1:
        lista.append(1)
    else:
        lista.append(lista[-1]+lista[-2])
n = lista[-1]

print("Kanipariskuntia on {0} kuukauden kuluttua {1}".format(kuukausi,n))
print("Kiitos ohjelman käytöstä.")
