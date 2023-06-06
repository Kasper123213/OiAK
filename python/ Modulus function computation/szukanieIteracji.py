import math


def petla(x, p):
    liczbaIteracji = 0
    x = bin(x)[2:]

    n = len(x)
    r = math.ceil(math.log2(p))
    k = math.ceil(n / r)

    if len(x) < k * r:
        x = (k * r - n) * "0" + x

    xList = []

    for i in range(1, k + 1):
        xList.append(x[len(x) - i * r:len(x) - (i - 1) * r])

    s = 0
    for i in range(1, k + 1):
        s += int(xList[i - 1], 2) * (pow(2, r * (i - 1)) % p)

    s_temp = s

    while s_temp > 2 * p:
        liczbaIteracji += 1
        s_temp = bin(s_temp)[2:]
        n_temp = len(s_temp)
        k_temp = math.ceil(n_temp / r)

        if len(s_temp) < k_temp * r:
            s_temp = (k_temp * r - n_temp) * "0" + s_temp

        sList = []
        for i in range(1, k_temp + 1):
            sList.append(s_temp[len(s_temp) - i * r:len(s_temp) - (i - 1) * r])

        newS_temp = 0
        for i in range(1, k_temp + 1):
            newS_temp += int(sList[i - 1], 2) * (pow(2, r * (i - 1)) % p)
        s_temp = newS_temp
    return liczbaIteracji



def dopisz_do_pliku(liczby, nazwa_pliku):
    with open(nazwa_pliku, 'a') as plik:
        kolumna=''
        for x in liczby:
            kolumna = kolumna + str(x)
            kolumna = kolumna + "\t\t"
        # kolumna = ' '.join(str(x) for x in liczby)
        plik.write(kolumna + '\n')



nazwa_pliku = 'testy.txt'
# nazwa_pliku = nazwa_pliku[:5]+"3"+nazwa_pliku[5:]
# print(nazwa_pliku)

# dopisz_do_pliku(["x", "p", "liczbaIteracji"], nazwa_pliku)

x=1
while True:
    x+=1
    for p in range(2, x):
        liczbaIteracji = petla(x, p)

        if liczbaIteracji>=1:
            dopisz_do_pliku([x, p, liczbaIteracji], nazwa_pliku[:5]+str(liczbaIteracji)+nazwa_pliku[5:])
