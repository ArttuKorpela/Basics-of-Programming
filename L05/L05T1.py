
#Aliohjelmat
def tulostaOhjeet():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.\nTämä aliohjelma tulostaa ohjeita käyttäjälle.\nAnna nimesi kahdessa osassa.")
    return None
def kysyNimi(par1):
    print(par1)
    nimi=input("Anna etunimi: ")
    print(par1)
    sukunimi=input("Anna Sukunimi: ")
    kokonimi = f"{nimi} {sukunimi}"
    return kokonimi
def tulostaTulokset(nimi):
    print("Tämä aliohjelma tulostaa nimesi.")
    print(f"Hei {nimi}")
    return None
#Paaohjelma
def paaohjelma():
    tulostaOhjeet()
    kokonimi=kysyNimi("Tämä aliohjelma kysyy nimen.")
    tulostaTulokset(kokonimi)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()