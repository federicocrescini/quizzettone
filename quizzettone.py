from random import randint
import os
import time

os.system("clear")

def credit():
    print("- fede")

def quit():
    os.system("clear")
    print("gl per l'esame ;)")
    exit()

def stampa(x, c, r, t):
    if c == -1:
        os.system("clear") 

    if x == 'f':
        print("Punteggio: " + str(c) + " / 5")
        print()
        print("Le risposte corrette: " + str(r))
        print("Le tue risposte:      " + str(t))
        print()
        print("[N]ext  -  [M]enu")

    if x == 'a':
        print("╔════════════════════════════════════╗")
        print("║            ALGOTEST.py             ║")
        print("║         scegli una modalità        ║")
        print("╚════════════════════════════════════╝")
        print()
        print("1) Simulazione esame")
        print("2) Sandbox")
        print("3) Istruzioni")
        print("0) Uscita")

    if x =='e':
        print("╔═════════════════════════════════╗")
        print("║             -ESAME-             ║")
        print("║   5 domande, tra Vero / Falso   ║")
        print("║        e scelte multiple        ║")
        print("║                                 ║")
        print("║      0 = falso / non corretta   ║")
        print("║      1 = vera / corretta        ║")
        print("║      2 = ritorno al menu        ║")
        print("╚═════════════════════════════════╝")
        print()
    
    if x == 's':
        print("╔═══════════════════════════════════╗")
        print("║             -SANDBOX-             ║")
        print("║                                   ║")
        print("║      0 = falso / non corretta     ║")
        print("║      1 = vera / corretta          ║")
        print("║      2 = ritorno al menu          ║")
        print("╚═══════════════════════════════════╝")
    
    if x == 'sb':
        print("╔═══════════════════════════════════╗")
        print("║           -SANDBOX MENU-          ║")
        print("╚═══════════════════════════════════╝")
    
    if x =='i':
        print()
        print("non fare la fighetta")

    if x == 'ms':
        print("Scegliere la tipologia di domande:")
        print("   1) V - F")
        print("   2) Scelta multipla")
        print("   3) Entrambi")
        print("   0) Ritorno al menu")

    if x =='u':
        print("Uscita")
        time.sleep(0.3)
        os.system("clear")
        print("Uscita .")
        time.sleep(0.1)
        os.system("clear")
        print("Uscita . .")
        time.sleep(0.1)
        os.system("clear")
        print("Uscita . . .")
        time.sleep(0.3)
    print()

def quesito(mbs):
    r = [2] * 5
    x = os.path.getsize(filedaaprire)
    mp = x - 500
            # ^ ci va il numero di byte dell'ultima domanda
            # l'ultima domanda va inserita ripetuta
    f = open(filedaaprire, "r")

    while True:
        while x > mp: x = randint(1,mp)
        l = f.read(x)
        l = f.read(1)
        if(l == '!') : exit()
        scelte = ['-', '+']
        if mbs == '*':
            mbs = scelte[randint(0,1)]

        while "//" not in l:
            l = f.readline()
        if mbs != '-':
            while '++' not in l:
                if '!!' in l:
                    r = quesito(mbs)
                    return r
                l = f.readline()
        if mbs != '+':
            while '--' not in l:
                if '!!' in l:
                    r = quesito(mbs)
                    return r
                l = f.readline()
        domanda = f.readline()
        print("--------------------------------------")
        print(domanda)
        c = 0
        while True:
            l = f.readline()
            if "//" in l: break
            if "!!" in l: break
            print(str(c+1) + "." + l[1:-2])
            temp = l[-2:-1]
            r[c] = temp
            c += 1
        return r# mbs -> codice caratteriale per la distinzione nella pesca delle domande

def sb(mbs):
    if mbs != 'e':
        stampa('s', 0, 0, 0)
    else:
        mbs = '*'
    score = 0
    giuste = quesito(mbs)
    con = ['/'] * 5
    print()
    print("RISPOSTE: ")
    print("1 2 3 4 5")
    ris = input()
    print()
    if '2' in ris:
        return -1, 0, 0
    i = 0
    k = 0
    while k < 5 and i < len(ris):
        con[k] = ris[i]
        if con[k] == giuste[k]:
            score += 1
        i += 2
        k +=1
    return score, giuste, con

def fineRisposte(p, r, t, e):
    stampa('_',  0,  0,  0)
    if e == 1:
        stampa('f', p, r, t)
        return p, 0, 0, 0
    else:
        stampa('f', p, r, t)
        x = input()
        while x != 'N' and x != 'M' and x != 'n' and x != 'm':
            x = input("[N/M] ")
        
        if x == 'N' or x =='n':
            print("next")
            stampa("_", -1, 0, 0)
            #next
            return p
        if x == 'M' or x =='m':
            return -1


# stacca conferma - punteggio - nuova domanda
# utente inserisce dati + invio
    # refresh
    # "Punteggio: " + str(p) + " / 5"
    # soluzioni con risposte date / risposte corrette
    # tasto continua / esci / riprova


def sandbox():
    md = 4
    p = -1
    while md != '0':
        if p == -1:
            stampa('sb', -1, 0, 0)
            stampa('ms', 0, 0, 0)
            md = input()
            stampa('_', -1, 0, 0)
        if md == '1':
            p, giuste, tue = sb('+')
        if md == '2':
            p, giuste, tue = sb('-')
        if md == '3':
            p, giuste, tue = sb('*')
        if md != '1' and md != '2' and md != '3':
            print("!!!Inserire un valore corretto!!!")
        if p == -1:
            stampa('u', -1, 0, 0)
        else:
            p = fineRisposte(p, giuste, tue, 0)
    return           
    
def esame():
    stampa('e', -1, 0, 0)
    tuttetue  = [['/'] * 5 ] * 5
    tuttegiuste = [['/'] * 5 ] * 5
    
    tot = 0
    i = 0
    while i < 5:
        p, giuste, tue = sb('e')
        if p == -1:
            return
        tuttetue[i] = tue
        tuttegiuste[i] = giuste

        for idx, x in enumerate(giuste):
            #print(idx)
            if tuttetue[i][idx] == tuttegiuste[i][idx]:
                tot += 1 
        i+=1

    print()
    print("Punteggio: " + str(tot) + " / 25")
    print()
    print("Le risposte corrette: " + str(tuttegiuste))
    print("Le tue risposte:      " + str(tuttetue))
    print()
    print("[N]ext  -  [M]enu")
    
    x = input()
    while x != 'N' and x != 'M' and x != 'n' and x != 'm':
        x = input("[N/M] ")
    
    if x == 'N' or x =='n':
        stampa("_",  -1, 0, 0)
        return esame()
    
    if x == 'M' or x =='m':
        return 

def menu():
    if os.path.exists(filedaaprire) == False:
        print(" !!! Errore, file non letto !!! ")
        exit()
    stampa('a', -1, 0, 0)
    while True:
        scelta = input("> ")
        
        if scelta == '0':
            quit()
        if scelta == '3':
            stampa('i', 0, 0, 0)
        else:
            if scelta == '1':
                esame()
            else:
                if scelta == '2':
                    sandbox()
                else :
                    if scelta == 'credit':
                        credit()
                    else:
                        print("Selezionare un'opzione valida")
            stampa('a', -1, 0, 0)


filedaaprire = input("Nome / percorso del file con le domande: ")
menu()
