print("Tämä ohjelma laskee neljän tenttiarvosanan keskiarvon.")
arvosana1 = (input("Anna 1. tenttiarvosana väliltä 0-5: "))
arvosana2 = (input("Anna 2. tenttiarvosana väliltä 0-5: "))
arvosana3 = (input("Anna 3. tenttiarvosana väliltä 0-5: "))
arvosana4 = (input("Anna 4. tenttiarvosana väliltä 0-5: "))
print()
summa = (int(arvosana1)+int(arvosana2)+int(arvosana3)+int(arvosana4))
keskiarvo = summa/4

print(f"Antamiesi arvosanojen summa on {summa}.")
print(f"Antamiesi arvosanojen keskiarvo on {round(keskiarvo,1)}.")
print(f"Keskiarvo on kokonaislukuna {int(keskiarvo)}.")
print("Kiitos ohjelman käytöstä.")
