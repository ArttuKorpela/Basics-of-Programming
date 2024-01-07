#alioohjelmat
def testaus(riviraw):
    skip=False
    palidromi=True
    lyhyt=False
    lopsana=""
    rivi=(riviraw[:-1]).lower()
    if rivi.startswith("#")==True:
        palidromi=False
    elif len(rivi) < 2:
        palidromi=False
    if True:
        for i in range(len(rivi)):
            if rivi[i].isdigit() == True:
                palidromi = False
            elif rivi[i].isalpha() == True:
                lopsana+=rivi[i]

        if lopsana == lopsana[::-1] and lopsana != "" and palidromi==True:
            palidromi = True
            print(f"OK: '{riviraw[:-1]}'")
        else:
            print(f"Ei OK: '{riviraw[:-1]}'")
            palidromi=False
    n="1"
    jono=[lopsana,riviraw[:-1]]
    if palidromi == True:
        return jono
    elif riviraw=="":
        return ""
    else:
        return n

def kirjoitus(tiedostonNimi,alkprnPali,siistittyPali,rivi):
    kirjoitusFile=open(tiedostonNimi,"a",encoding="utf-8")
    kirjoitusFile.write(siistittyPali+"\n")
    kirjoitusFile.write(("----> "+alkprnPali+"\n"))
    rivi=rivi
    kirjoitusFile.close()
    return None
#Paaohjelma

def paaohjelma():
    lt=input("Anna luettavan tiedoston nimi: ")
    kt=input("Anna kirjoitettavan tiedoston nimi: ")

    kirTied=open(kt,"w",encoding="utf-8")
    kirTied.close()
    lueTied=open(lt,"r",encoding="utf-8")
    rivi=""
    while True:
        rivi_n=lueTied.readline()
        if rivi_n=="":
            break
        rivi=rivi_n
        n=testaus(rivi)
        if n[0]!="1":
            kirjoitus(kt,n[0],n[1],1)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()



