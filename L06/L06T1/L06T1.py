#L06T1
#Arttu Korpela

#aliohjelmat

def tiedostoKirjoita(TiedostonNimi,):
    tiedosto= open(TiedostonNimi,"w",encoding="utf-8")
    while True:
        talNimi=input("Anna tiedostoon tallennettava nimi (enter lopettaa): ")
        if talNimi=="":
            tiedosto.close()
            break
        else:
            tiedosto.write(talNimi + "\n")
    return None



def tiedostoLue(TiedostonNimi,):
    tiedosto = open(TiedostonNimi, "r", encoding="utf-8")
    print(f"Tiedostoon '{TiedostonNimi}' on tallennettu seuraavat nimet:")
    while True:
        rivi=tiedosto.readline()
        if rivi=="":
            tiedosto.close()
            break
        else:
            print(rivi[:-1])
    return None




#paaohjelma

def paaohjelma():
    tiedoston_nimi=input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(tiedoston_nimi)
    tiedostoLue(tiedoston_nimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()