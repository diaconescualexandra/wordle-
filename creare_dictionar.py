m = 0
guess=0
dictionar_cuvinte={c:0 for c in lista_cuvinte}
cuvinte_opener=[]
with open ("cuvinte.out", "w") as g:
    for c in lista_noua:
        print(c)
        s=0
        cuvinte_opener=[]
        cheie=c
        gasit=0
        lista_cuvinte=lista_noua
        while gasit == 0:
            litere_eliminat = []
            feedback = []
            if m == 0:
                opener = "CAREI"
                m = 1
                cuvinte_opener.append("CAREI")
            elif m == 1:
                if len(lista_cuvinte)==1:
                    opener=lista_cuvinte[0]
                    cuvinte_opener.append(opener)
                else:
                    opener = entropie(lista_cuvinte)
                    cuvinte_opener.append(opener)
            #print(opener)

            if opener == cheie:
                gasit = 1
                lista_cuvinte=['v']*5
                #print(*lista_cuvinte)

            else:
                feedback = functie(cheie, opener)
                p = 0
                #print(*feedback)
                for l in feedback:
                    if l == 'n':
                        litere_eliminat.append(opener[p])
                    p = p + 1

                #print(litere_eliminat)
                cuvinte2 = []
                for c in lista_cuvinte:
                    ok = 1
                    for i in c:
                        if i in litere_eliminat:
                            ok = 0
                    for i in range(5):
                        if feedback[i]=='g':
                            if c[i] == opener[i]:
                                ok=0
                    for i in range(5):
                        if feedback[i]=='v':
                            if c[i] != opener[i]:
                                ok=0
                    if ok == 1:
                        cuvinte2.append(c)

                lista_cuvinte = cuvinte2
                #print(lista_cuvinte)
                cuvinte2 = []
        dictionar_cuvinte[c]=cuvinte_opener
        g.write(c)
        g.write("\n")
        g.write(str(dictionar_cuvinte[c]))
        g.write("\n")
        print(dictionar_cuvinte[c])
        print("\n")
