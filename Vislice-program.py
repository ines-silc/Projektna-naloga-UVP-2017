import random
import tkinter as tk

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

stevec_napacnih = 0

def nova_igra(pop_up_okence):
    slika.delete("all")
    beseda = random.choice(besede_v_seznam('Besede.txt'))
    vzorec = izpisi_vzorec()
    polje.config(text=' '.join(vzorec))
    stevec_napacnih = 0
    pop_up_okence.destroy()
    
def spremeni_vzorec(crka):
    if crka in razdeljena_beseda:
        for i, value in enumerate(razdeljena_beseda):
            if value == str(crka):
                vzorec[i] = value.replace('__', crka)
        polje.config(text=' '.join(vzorec))
        if razdeljena_beseda == vzorec:
            zakljucek = tk.Toplevel()
            zakljucek.title('KONEC IGRE!')
            poskusi = tk.Message(zakljucek, text='Zmagal si, čestitamo!')
            poskusi.pack()
            b = tk.Button(zakljucek, text='Nova igra',
                          command = lambda:nova_igra(zakljucek))
            b.pack()
    else:
        global stevec_napacnih
        stevec_napacnih += 1
        if stevec_napacnih > 0:
            slika.create_oval(30, 160, 120, 250)
        if stevec_napacnih > 1:
            slika.create_line(75, 160, 75, 50)
        if stevec_napacnih > 2:
            slika.create_line(75, 50, 150, 50)
        if stevec_napacnih > 3:
            slika.create_line(150, 50, 150, 80)
        if stevec_napacnih > 4:
            slika.create_oval(140, 80, 160, 100)
        if stevec_napacnih > 5:
            slika.create_line(150, 100, 150, 140)
        if stevec_napacnih > 6:
            slika.create_line(150, 115, 160, 125)
        if stevec_napacnih > 7:
            slika.create_line(150, 115, 140, 125)
        if stevec_napacnih > 8:
            slika.create_line(150, 140, 160, 150)
        if stevec_napacnih > 9:
            slika.create_line(150, 140, 140, 150)
            slika.create_oval(140, 80, 160, 100, fill = 'red')
            zakljucek = tk.Toplevel()
            zakljucek.title('KONEC IGRE!')
            poskusi = tk.Message(zakljucek, text='Izgubil si!')
            poskusi.pack()
            b = tk.Button(zakljucek, text='Nova igra',
                          command= lambda: nova_igra(zakljucek))
            b.pack()
            

okno = tk.Tk()
polje = tk.Label(text=' '.join(vzorec))
polje.grid(row = 1, column = 1, columnspan = 10)
a = tk.Button(okno, text = 'A', command = lambda:spremeni_vzorec('A'))
a.grid(row = 2, column = 1)

b = tk.Button(okno, text = 'B', command = lambda:spremeni_vzorec('B'))
b.grid(row = 2, column = 2)
c = tk.Button(okno, text = 'C', command = lambda:spremeni_vzorec('C'))
c.grid(row = 2, column = 3)
č = tk.Button(okno, text = 'Č', command = lambda:spremeni_vzorec('Č'))
č.grid(row = 2, column = 4)
d = tk.Button(okno, text = 'D', command = lambda:spremeni_vzorec('D'))
d.grid(row = 2, column = 5)
e = tk.Button(okno, text = 'E', command = lambda:spremeni_vzorec('E'))
e.grid(row = 2, column = 6)
f = tk.Button(okno, text = 'F', command = lambda:spremeni_vzorec('F'))
f.grid(row = 2, column = 7)
g = tk.Button(okno, text = 'G', command = lambda:spremeni_vzorec('G'))
g.grid(row = 2, column = 8)
h = tk.Button(okno, text = 'H', command = lambda:spremeni_vzorec('H'))
h.grid(row = 2, column = 9)
i = tk.Button(okno, text = 'I', command = lambda:spremeni_vzorec('I'))
i.grid(row = 2, column = 10)
j = tk.Button(okno, text = 'J', command = lambda:spremeni_vzorec('J'))
j.grid(row = 3, column = 1)
k = tk.Button(okno, text = 'K', command = lambda:spremeni_vzorec('K'))
k.grid(row = 3, column = 2)
l = tk.Button(okno, text = 'L', command = lambda:spremeni_vzorec('L'))
l.grid(row = 3, column = 3)
m = tk.Button(okno, text = 'M', command = lambda:spremeni_vzorec('M'))
m.grid(row = 3, column = 4)
n = tk.Button(okno, text = 'N', command = lambda:spremeni_vzorec('N'))
n.grid(row = 3, column = 5)
o = tk.Button(okno, text = 'O', command = lambda:spremeni_vzorec('O'))
o.grid(row = 3, column = 6)
p = tk.Button(okno, text = 'P', command = lambda:spremeni_vzorec('P'))
p.grid(row = 3, column = 7)
r = tk.Button(okno, text = 'R', command = lambda:spremeni_vzorec('R'))
r.grid(row = 3, column = 8)
s = tk.Button(okno, text = 'S', command = lambda:spremeni_vzorec('S'))
s.grid(row = 3, column = 9)
š = tk.Button(okno, text = 'Š', command = lambda:spremeni_vzorec('Š'))
š.grid(row = 3, column = 10)
t = tk.Button(okno, text = 'T', command = lambda:spremeni_vzorec('T'))
t.grid(row = 4, column = 3)
u = tk.Button(okno, text = 'U', command = lambda:spremeni_vzorec('U'))
u.grid(row = 4, column = 4)
v = tk.Button(okno, text = 'V', command = lambda:spremeni_vzorec('V'))
v.grid(row = 4, column = 5)
z = tk.Button(okno, text = 'Z', command = lambda:spremeni_vzorec('Z'))
z.grid(row = 4, column = 6)
ž = tk.Button(okno, text = 'Ž', command = lambda:spremeni_vzorec('Ž'))
ž.grid(row = 4, column = 7)

slika = tk.Canvas(height=200, width=200, bd=1,
                  highlightthickness=1, relief='ridge')
slika.grid(row = 5, column = 1, columnspan = 10)


okno.mainloop()
