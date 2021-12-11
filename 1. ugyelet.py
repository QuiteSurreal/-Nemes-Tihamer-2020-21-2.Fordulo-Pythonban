from sys import stdin, stdout

def main():
    hanynap, hanyember = map(int, stdin.readline().split())
    napok = (list(map(int, stdin.readline().split())))
    kezdet = 0
    veg = 0
    fointervallum = 100000
    fokezdet = 0
    szamok = []
    kovnapok = []
    for i in range(hanyember):
        szamok.append(int(i+1))
    kovnapok = szamok.copy()
    intervallum = 1
    for i in range(hanynap):
        if kovnapok == szamok:
            kezdet = i
        if napok[i] in kovnapok:
            kovnapok.remove(napok[i])
            if len(kovnapok) == 0:
                if intervallum < fointervallum:
                    veg = i+1
                    intervallum = 0
                    visszahely = 0
                    kovnapok = szamok.copy()
                    szuknap = napok.copy()
                    kezdet = 1
                    del szuknap[veg:]
                    visszanapok = []
                    for j in reversed(szuknap):
                        visszanapok.append(j)
                    for k in range(hanyember):
                        if szuknap.index(k + 1) + 1 > visszahely:
                            fokezdet = i - visszanapok.index(k + 1) - 1
                            fointervallum = veg-fokezdet
                            #print(fokezdet, veg)
                            visszahely = visszanapok.index(k + 1) + 1
        intervallum += 1
    if fointervallum == 100000:
        print("-1")
    #print(fointervallum)
    stdout.write("\n" + str(fokezdet) + " " + str(veg) + "\n")

main()