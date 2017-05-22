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

def spremeni_vzorec(crka):
    if str(crka) in razdeljena_beseda:
        for i, value in enumerate(razdeljena_beseda):
            if value == str(crka):
                vzorec[i] = value.replace('__', str(crka))
    else:
        crka = nova_crka = input('Nova črka? ')
        for i, value in enumerate(razdeljena_beseda):
            if value == str(nova_crka):
                vzorec[i] = value.replace('__', str(nova_crka))
    return vzorec
    
import tkinter as tk

okno = tk.Tk()
polje = tk.Entry

a = tk.Button(okno, text = 'A')
a.pack()
a.grid(row = 2, column = 1)
b = tk.Button(okno, text = 'B')
b.grid(row = 2, column = 2)
c = tk.Button(okno, text = 'C')
c.grid(row = 2, column = 3)
d = tk.Button(okno, text = 'D')
d.grid(row = 2, column = 4)
e = tk.Button(okno, text = 'E')
e.grid(row = 2, column = 5)
f = tk.Button(okno, text = 'F')
f.grid(row = 2, column = 6)
g = tk.Button(okno, text = 'G')
g.grid(row = 2, column = 7)
h = tk.Button(okno, text = 'H')
h.grid(row = 2, column = 8)
i = tk.Button(okno, text = 'I')
i.grid(row = 2, column = 9)
okno.mainloop()

