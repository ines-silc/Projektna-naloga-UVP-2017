import random

def besede_v_seznam(ime_dadoteke):
    seznam_besed = []
    with open(ime_dadoteke) as besede:
        for vrstica in besede:
            s2 = vrstica.strip()
            seznam_besed.append(s2)
    return seznam_besed

seznam_besed = besede_v_seznam('Besede.txt')

beseda = random.choice(besede_v_seznam('Besede.txt'))

def izpisi_vzorec():
    vzorec = []
    for x in range(len(beseda)):
        vzorec.append('__')
    return vzorec

def razdeli_besedo(beseda):
    seznam_crk = []
    for x in beseda:
        seznam_crk.append(x)
    return seznam_crk

razdeljena_beseda = razdeli_besedo(beseda)

vzorec = izpisi_vzorec()

def vzemi_crko():
    vnesena_crka = input()
    print(vnesena_crka)

def spremeni_vzorec():
    for x in razdeljena_beseda:
        if vnesena_crka == x:
            vzorec[x] = vnesena_crka
        else:
            print('neveljavno')
    return vzorec
        
