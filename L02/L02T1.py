nimi = input("Mikä nimesi on: ")
kanta = input("Anna kolmion kanta kokonaislukuna: ")
korkeus = input("Anna kolmion korkeus desimaalilukuna: ")

print(f'{nimi} annoit kannaksi {kanta} ja korkeudeksi {round(float(korkeus),1)}')
print(f'Kolmion pinta-ala on tällöin {(int(kanta)*float(korkeus))/2}')
print("Kiitos ohjelman käytöstä.")