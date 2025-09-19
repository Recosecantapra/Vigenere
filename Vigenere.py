a, b = "0123456789abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ.,=:;-_'^¨*?+[]()}{&%¤$#£@ ", {}
bLIST, nLIST, fLIST = [], [], []

besked = input("Skriv en besked: ")
nøgle = input("Skriv en nøgle: ")

for i in a:
    b[i]=a.index(i)+1

def krypter(bes, nøg):
    for l in bes:
        bLIST.append(b[l])
    for w in nøg:
        nLIST.append(b[w])
    for i in range(len(bes)):
        fLIST.append((bLIST[i] + nLIST[i])%95)


krypter(besked, nøgle)
print(fLIST)