print("Tämä ohjelma laskee risteilyhintoja.")
hytti=input("Minkälainen hytti on kyseessä - A, B vai C-hytti: ")
sesonki=input("Onko sesonkiaika (k/e): ")
kanta=input("Onko kanta-asiakas (k/e): ")
hinta=79
if hytti.lower()=="c":
    hinta=hinta
    if sesonki.lower() == "k":
        hinta = hinta * 1.5
    else:
        hinta=hinta
elif hytti.lower()=="b":
    hinta=round(hinta*1.1,0)
    if sesonki.lower() == "k":
        hinta = hinta * 1.75
    else:
        hinta=hinta
elif hytti.lower()=="a":
    hinta=round(hinta*1.60,0)
    if sesonki.lower() == "k":
        hinta = hinta*2.75
    else:
        hinta=hinta
if kanta.lower()=="k":
    hinta=hinta*0.9
else:
    hinta=hinta
print(f"{hytti.upper()}-hytti maksaa {round(hinta,2)} euroa.")
print("Kiitos ohjelman käytöstä.")
