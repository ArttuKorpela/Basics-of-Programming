print("Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.")
paino_kg = float(input("Anna paino kiloina: "))
print(f"Paino on {paino_kg} kg eli {round(paino_kg/0.4536,1)} naulaa.\n")

pituus_cm = int(input("Anna pituus sentteinä: "))
print("Pituus on",str(round(pituus_cm/100,2)),"metriä ",end="")
print("eli amerikkalaisittain",round(float(int(pituus_cm/30.48)),1),'jalkaa ',end="")
print('ja',round((pituus_cm%30.48)/2.54,1),"tuumaa.")
print("Kiitos ohjelman käytöstä.")
