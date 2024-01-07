yht=0
ala=0
while True:
    syote=float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
    if syote==0 and yht==0:
        print("Väärä syöte. Painon tulee olla 30 ja 130 kg välillä (0 lopettaa).")
    elif syote==0:
        print(f"Painojen keskiarvo on {round(yht/ala,1)}.")
        print("Kiitos ohjelman käytöstä.")
        break
    elif syote<30 or syote>130:
        print("Väärä syöte. Painon tulee olla 30 ja 130 kg välillä (0 lopettaa).")
    else:
        yht+=syote
        ala+=1

