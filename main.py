#f = open("fisierintrare.txt")
#lista=[]
#for linie in f.readlines():
    #lista.append([x for x in linie.split()])
#f.close()
#for i in range (len(lista)-1):
    #lista[i][1]=int(lista[i][1])
#print(lista)

tabela_stari_nfa={}
with open('fisierintrare.txt') as file:
    stare_initiala = file.readline().replace('\n', '')
    stari_finale = file.readline().replace('\n', '').split()
    print(stari_finale)
    for line in file:
        line = line.replace('\n', '').split(' ')
        sursa, litera, destinatie = line
        if sursa not in tabela_stari_nfa:
            tabela_stari_nfa[sursa]={}
        if litera not in tabela_stari_nfa[sursa]:
            tabela_stari_nfa[sursa][litera] = [destinatie]
        else:
            tabela_stari_nfa[sursa][litera] += [destinatie]
print(tabela_stari_nfa)
stare_curenta = stare_initiala
cuv = input()
Drum=[]
if cuv=='vid':
    if stare_curenta in stari_finale:
        print("acceptat")
        print("->", end='')
        print(stare_curenta)
    else:
        print("respins")
else:
    try:
        for i in range (len(cuv)):
            Drum.append(stare_curenta)
            stare_curenta = tabela_stari_nfa[stare_curenta][cuv[i]][0]
        Drum.append(stare_curenta)
        if stare_curenta in stari_finale:
            print("acceptat")
            print("->", end='')
            for stare in Drum:
                print(stare, end="->")
        else:
            print("respins")
    except KeyError:
        print("respins")