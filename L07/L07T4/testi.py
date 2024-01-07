def analyysi(olio,lista):
    olio.pieninarvo=min(lista)
    olio.suurinarvo=max(lista)
    olio.summa=sum(lista)
    olio.keskiarvo=(sum(lista))/len(lista)
    return