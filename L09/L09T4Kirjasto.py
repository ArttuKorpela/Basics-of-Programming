Versio = 1.0

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto\n2) Analysoi\n3) Kirjoita tiedosto\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyTied(kehote,tiedostonNimi):
    print(f"{kehote} tiedoston nimi on '{tiedostonNimi}'.")
    luku1 =input("Anna uusi nimi, enter säilyttää nykyisen: ")
    return luku1

def lueTiedosto(luettavanTiedostonNimi):
    lista=[]
    lt=open(luettavanTiedostonNimi,"r",encoding="utf-8")
    while True:
        rivi=((lt.readline())[:-1])
        if rivi=="":
            break
        lista.append(int(rivi))
    lt.close()
    return lista

def analyysi(olio,lista):
    olio.pieninarvo=min(lista)
    olio.suurinarvo=max(lista)
    olio.summa=sum(lista)
    olio.keskiarvo=round(sum(lista)/len(lista),0)
    return olio


def kirjoitus(tiedostonNimi,olio):
    tiedosto=open(tiedostonNimi,"w",encoding="utf-8")
    tiedosto.write("Analyysin tulokset ovat seuraavat:\n"
                   "Datan pienin arvo on {0}.\n"
                   "Datan suurin arvo on {1}.\n"
                   "Datan summa on {2}.\n"
                   "Datan keskiarvo on {3:.1f}.".format(olio.pieninarvo,olio.suurinarvo,olio.summa,olio.keskiarvo))
    tiedosto.close()
    return None
