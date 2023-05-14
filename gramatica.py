with open("gramatica.txt", "r") as grammar_file:
    grammar = {}
    for line in grammar_file:
        productions = line.split()
        grammar[productions[0]] = productions[1:]

with open("cuvinte.txt", "r") as words_file:
    cuvinte = []
    for word in words_file:
        cuvinte.append(word.strip('\n'))

#print(grammar)
#print(cuvinte)

for cuvant in cuvinte:
    cuvinte_posibile=[]
    for productie in grammar['S']:
        if cuvant[0] == productie[0]:
            cuvinte_posibile.append(productie)
    while(cuvinte_posibile):
        cuvant_posibil = cuvinte_posibile[0]
        #print(cuvinte_posibile)
        #print(cuvant_posibil)
        if len(cuvant_posibil) > len(cuvant) + 2 :
            print('neacceptat')
            break
        try:
            if cuvant == cuvant_posibil[:-1] and 'lambda' in grammar[cuvant_posibil[-1]]:
                print('acceptat')
                break
            else:
                for productie in grammar[cuvant_posibil[-1]]:
                    if productie != 'lambda':
                        cuvinte_posibile.append((cuvant_posibil[:-1]) + productie)
                cuvinte_posibile.pop(0)
        except KeyError:
            if cuvant == cuvant_posibil:
                print('acceptat')
                break
            cuvinte_posibile.pop(0)
    if cuvinte_posibile == []:
        print('neacceptat')
