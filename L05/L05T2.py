
#aliohjelat
def tulostaOhjeet():
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.\nOhjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi\nlukujen lukumäärän.")
    print()
    return None
def kysyLuku(KayttajaPyynto):
    luku=input(KayttajaPyynto)
    return luku
def vertaileLukuja(x,y):
    if x<y:
        pienempiLuku=x
    else:
        pienempiLuku=y
    return pienempiLuku
def tulostaTiedot(pieninLuku,lukujenMaara):
    if lukujenMaara==1:
        print()
        print(f"Annoit yhden luvun, joka oli {pieninLuku}.")
    elif lukujenMaara=="muu":
        print(f"Annetuista luvuista pienempi oli {pieninLuku}.")
    else:
        print()
        print(f"Annoit {lukujenMaara} lukua.")
        print(f"Annetuista luvuista pienin oli {pieninLuku}.")
#paaohjelma
def paaohjelma():
    lukujenmaara=0
    pieninluku=0
    tulostaOhjeet()
    pieninluku = kysyLuku("Anna positiivinen kokonaisluku: ")
    lukujenmaara += 1
    uusiluku = kysyLuku("Anna vertailtava positiivinen kokonaisluku (0 lopettaa): ")
    if uusiluku == "0":
        tulostaTiedot(pieninluku, lukujenmaara)
        print("Kiitos ohjelman käytöstä.")
    else:
        pieninluku = vertaileLukuja(pieninluku, uusiluku)
        lukujenmaara += 1
        tulostaTiedot(pieninluku, "muu")
        while pieninluku != 0:
            uusiluku = kysyLuku("Anna uusi positiivinen kokonaisluku (0 lopettaa): ")
            if uusiluku == "0":
                tulostaTiedot(pieninluku, lukujenmaara)
                print("Kiitos ohjelman käytöstä.")
                break
            else:
                pieninluku = vertaileLukuja(pieninluku, uusiluku)
                lukujenmaara += 1
                tulostaTiedot(pieninluku, "muu")



paaohjelma()