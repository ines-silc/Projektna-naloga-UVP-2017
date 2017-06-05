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
    if crka in razdeljena_beseda:
        for i, value in enumerate(razdeljena_beseda):
            if value == str(crka):
                vzorec[i] = value.replace('__', crka)
    else:
        pass
    return vzorec
    
import tkinter as tk

okno = tk.Tk()
polje = tk.Label(text=' '.join(vzorec))
polje.grid(row = 1, column = 5)
a = tk.Button(okno, text = 'A', command = spremeni_vzorec('A'))
a.grid(row = 2, column = 1)
b = tk.Button(okno, text = 'B', command = spremeni_vzorec('B'))
b.grid(row = 2, column = 2)
c = tk.Button(okno, text = 'C', command = spremeni_vzorec('C'))
c.grid(row = 2, column = 3)
č = tk.Button(okno, text = 'Č', command = spremeni_vzorec('Č'))
č.grid(row = 2, column = 4)
d = tk.Button(okno, text = 'D', command = spremeni_vzorec('D'))
d.grid(row = 2, column = 5)
e = tk.Button(okno, text = 'E', command = spremeni_vzorec('E'))
e.grid(row = 2, column = 6)
f = tk.Button(okno, text = 'F', command = spremeni_vzorec('F'))
f.grid(row = 2, column = 7)
g = tk.Button(okno, text = 'G', command = spremeni_vzorec('G'))
g.grid(row = 2, column = 8)
h = tk.Button(okno, text = 'H', command = spremeni_vzorec('H'))
h.grid(row = 2, column = 9)
i = tk.Button(okno, text = 'I', command = spremeni_vzorec('I'))
i.grid(row = 2, column = 10)
j = tk.Button(okno, text = 'J', command = spremeni_vzorec('J'))
j.grid(row = 3, column = 1)
k = tk.Button(okno, text = 'K', command = spremeni_vzorec('K'))
k.grid(row = 3, column = 2)
l = tk.Button(okno, text = 'L', command = spremeni_vzorec('L'))
l.grid(row = 3, column = 3)
m = tk.Button(okno, text = 'M', command = spremeni_vzorec('M'))
m.grid(row = 3, column = 4)
n = tk.Button(okno, text = 'N', command = spremeni_vzorec('N'))
n.grid(row = 3, column = 5)
o = tk.Button(okno, text = 'O', command = spremeni_vzorec('O'))
o.grid(row = 3, column = 6)
p = tk.Button(okno, text = 'P', command = spremeni_vzorec('P'))
p.grid(row = 3, column = 7)
r = tk.Button(okno, text = 'R', command = spremeni_vzorec('R'))
r.grid(row = 3, column = 8)
s = tk.Button(okno, text = 'S', command = spremeni_vzorec('S'))
s.grid(row = 3, column = 9)
š = tk.Button(okno, text = 'Š', command = spremeni_vzorec('Š'))
š.grid(row = 3, column = 10)
t = tk.Button(okno, text = 'T', command = spremeni_vzorec('T'))
t.grid(row = 4, column = 1)
u = tk.Button(okno, text = 'U', command = spremeni_vzorec('U'))
u.grid(row = 4, column = 2)
v = tk.Button(okno, text = 'V', command = spremeni_vzorec('V'))
v.grid(row = 4, column = 3)
z = tk.Button(okno, text = 'Z', command = spremeni_vzorec('Z'))
z.grid(row = 4, column = 4)
ž = tk.Button(okno, text = 'Ž', command = spremeni_vzorec('Ž'))
ž.grid(row = 4, column = 5)


okno.mainloop()

