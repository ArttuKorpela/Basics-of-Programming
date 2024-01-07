print("Tämä ohjelma etsii luvuilla 5 ja 7 jaollista lukua annetulta lukualueelta.")
ala=int(input("Anna lukualueen alaraja: "))
yla=int(input("Anna lukualueen yläraja: "))
onnistuminen=False


for numero in range(ala,yla+1):
    if numero%5==0 and numero%7==0:
        print(f"Luku {numero} on jaollinen 5:llä ja 7:llä.\nLopetetaan etsintä.")
        onnistuminen=True
        break
    elif numero%5!=0:
        print(f"{numero} ei ole jaollinen viidellä, hylätään.")
    elif numero%7!=0:
        print(f"{numero} ei ole jaollinen seitsemällä, hylätään.")
if onnistuminen==False:
    print("Alueelta ei löytynyt sopivaa lukua.")
print("Kiitos ohjelman käytöstä.")