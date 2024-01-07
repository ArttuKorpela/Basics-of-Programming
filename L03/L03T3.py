print("Selvitetään tuotteen alennusprosentti ja myyntihinta.")
hinta = float(input("Mikä on tuotteen listahinta: "))
print("Lasketaanko hinta")
print("1) yhdellä monihaaraisella valintarakenteella")
print("2) useilla erillisillä valintarakenteilla?")
valinta=input("Anna valintasi: ")
if valinta=="2":
    if hinta>=300:
        alennus="30%"
        hinta= hinta * 0.70
    if hinta>=200:
        alennus="20%"
        hinta= hinta * 0.80
    if hinta>=100:
        alennus="10%"
        hinta= hinta * 0.90
    else:
        alennus="0%"
        hinta=hinta
    print(f"Monella erillisellä valintarakenteella tulokset ovat seuraavat:")
    print(f"Tuotteen alennus on {alennus} ja hinnaksi jää {round(hinta, 2)}e.")
elif valinta=="1":
    if hinta>=300:
        alennus="30%"
        hinta= hinta * 0.70
    elif hinta>=200:
        alennus="20%"
        hinta= hinta * 0.80
    elif hinta>=100:
        alennus="10%"
        hinta= hinta * 0.90
    else:
        alennus="0%"
        hinta=hinta
    print(f"Yhdellä monihaaraisella valintarakenteella tulokset ovat seuraavat:")
    print(f"Tuotteen alennus on {alennus} ja hinnaksi jää {round(hinta, 2)}e.")

else:
    print("Tuntematon valinta.")
    print("Tuotteen alennus on 0% ja hinnaksi jää 100.0e.")
print("Kiitos ohjelman käytöstä.")
