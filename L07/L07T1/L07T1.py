######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Arttu Korpela
# Opiskelijanumero:1155912
# Päivämäärä:22.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla
#https://lutpub.lut.fi/handle/10024/162088
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lisää tuote listaan")    
    print("2) Poista tuote listasta")
    print("0) Lopeta")
    valinta=(input("Valintasi: "))
    return valinta

def lisaaTuote(ostoslista):
    
    tuote=input("Anna lisättävä tuote: ")
    ostoslista.append(tuote)
    print()
    return ostoslista

def poistaTuote(ostoslista):
    print("Ostoslistassasi on {0} tuotetta.".format(len(ostoslista)))
    poistettavaNum=(int(input("Anna poistettavan tuotteen järjestysnumero: "))-1)
    if poistettavaNum>len(ostoslista)-1:
        print(f"Indeksiä {poistettavaNum+1} ei löydy.")
        print("Tuotteiden järjestysnumerot alkavat numerosta 1.")   
    else:
        n=ostoslista[poistettavaNum]
        ostoslista.remove(n)
    print()
    return ostoslista

def tulostus(ostoslista):
    m=""
    print("Lopetetaan") 
    print("Sinulta jäi ostamatta seuraavat tuotteet:")
    for item in ostoslista:
        m+=(item+" ")
    print(m)
    print()
    return None

def sisalto(ostoslista):
    kaikki=""
    print("Ostoslistasi sisältää seuraavat tuotteet:")
    
    for i in ostoslista:
        kaikki+=(i+" ")
        
    print(kaikki)
    return None










def paaohjelma():
    ostoslista=[]
    valinta=0
    while True:
        sisalto(ostoslista)
        valinta=int(valikko())

        if valinta==1:
            ostoslista=lisaaTuote(ostoslista)
        elif valinta==2:
            ostoslista=poistaTuote(ostoslista)
        elif valinta==0:
            tulostus(ostoslista)
            break
        else:
            print("Tuntematon valinta yritä uudestaan.")
            print()
    
    print("Kiitos ohjelman käytöstä.")

paaohjelma()




# Tehtävä L07T1.py
# eof
