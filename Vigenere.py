a, b = "0123456789abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ.,=:;-_'^¨*?+[]()}{&%¤$#£@ ", {}
bLIST, nLIST, fLIST, gLIST = [], [], [], []
dbLIST, dnLIST, dfLIST, dgLIST = [], [], [], []

for i in a:
    b[i]=a.index(i)+1

def krypter(bes, nøg):
    for l in bes:
        bLIST.append(b[l])
    for w in nøg:
        nLIST.append(b[w])
    for i in range(len(bes)):
        fLIST.append((bLIST[i] + nLIST[i])%95)
    for v in fLIST:
        for c,d in b.items():
            if d == v:
                gLIST.append(c)

def dekrypter(bes, nøg):
    for l in bes:
        dbLIST.append(b[l])
    for w in nøg:
        dnLIST.append(b[w])
    for i in range(len(bes)):
        dfLIST.append((dbLIST[i] - dnLIST[i]))
    for v in dfLIST:
        for c,d in b.items():
            if d == v:
                dgLIST.append(c)

spørgsmål = input("Hvil du kryptere eller dekryptere? Skriv k eller d: ")

if spørgsmål == "k":
    besked = input("Skriv en besked: ")
    nøgle = input("Skriv en nøgle: ")
    krypter(besked, nøgle)
    whopper = "".join(gLIST)
    print(whopper)
elif spørgsmål == "d":
    kbesked = input("Skriv den krypterede besked: ")
    knøgle = input("Skriv nøglen: ")
    dekrypter(kbesked, knøgle)
    dwhopper = "".join(dgLIST)
    print(dwhopper)




