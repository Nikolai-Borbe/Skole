print("Tillegg: Og, videre, dessuten, for eksempel...")
print("Kontrast: Men, selv om, enda...")
print("Tid: Da, når, mens, så, deretter...")
print("Resultat, årsak, sammenheng: For, fordi, så, da, derfor...")
print("Oppregnende: For det første, med andre ord...")
print(" ")

tillegg = ("Og, videre, forresten, dessuten, for eksempel, spesielt, også, på samme måte, helt likt, men like viktig er, og ikke bare ... men også, sammen med, i lys av, for ikke å nevne, så vel som, på samme måte, relativt, tilsvarende, unikt, å si noe om")
kontrast = ("Men, selv om, enda, derimot, på tross av, trass i, imidlertid, likevel, istedenfor, tvert i mot, på den andre siden, i motsetning til, verken eller, foruten, for å si det på en annen måte")
tid = ("Da, når, mens, innen, før, etter, så, deretter, etterpå, endelig, senere, tidligere, samtidig, på den tid, ")
resultat = ("For, fordi, så, da, derfor, som et resultat, slik, slik at, hvis, altså, dermed, således, på grunn av, årsaken til")
oppregnende = ("For det første, for det andre, neste, da, i tillegg, det viktigste er at, med andre ord, for en ting, i første omgang")
konklusjon = ("i konklusjon, til slutt, alt i alt, altså, helt klart, faktisk, for å oppsummere, helt, selvfølgelig")

l1 = tillegg
l2 = kontrast
l3 = tid
l4 = resultat
l5 = oppregnende
l6 = konklusjon

def function1():
    print("l1 (tillegg), l2 (kontrast), l3 (tid), l4(resultat), l5 (oppregnende), l6 (konklusjon)")
    i = input(str("Hvilken liste?"))

    if i == str("l1"):
        print(" ")
        print(l1)
        print(" ")
    elif i == str("l2"):
        print(" ")
        print(l2)
        print(" ")
    elif i == str("l3"):
        print(" ")
        print(l3)
        print(" ")
    elif i == str("l4"):
        print(" ")
        print(l4)
        print(" ")
    elif i == str("l5"):
        print(" ")
        print(l5)
        print(" ")
    elif i == str("l6"):
        print(" ")
        print(l6)
        print(" ")
    else:
        print(" ")
        print("Sorry; you must have made a mistake; check your spelling.")
        print(" ")

while True:
    function1()
