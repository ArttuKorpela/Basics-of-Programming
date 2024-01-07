def testaus(riviraw):
    skip=False
    palidromi=False
    lopsana=""
    rivi=(riviraw[:-1]).lower()
    if rivi.startswith("#")==True:
        skip=True
    elif len(rivi) < 2:
        palidromi = False
    if skip==False:
        for i in range(len(rivi)):
            if rivi[i].isdigit() == True:
                palidromi = False
            elif rivi[i].isalpha() == True:
                lopsana+=rivi[i]
        if lopsana == lopsana[::-1] and lopsana != "":
            palidromi = True
            print(f"OK: {rivi}")
        elif palidromi == False:
            print(f"Ei OK: {rivi}")
    n=""
    if palidromi == True:
        return lopsana
    else:
        return n


