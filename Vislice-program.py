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

def izpisi_vzorec(beseda):
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

vzorec = izpisi_vzorec(beseda)

stevec_napacnih = 0

def nova_igra(pop_up_okence):
    global beseda
    global razdeljena_beseda
    global vzorec
    slika.delete("all")
    beseda = random.choice(besede_v_seznam('Besede.txt'))
    razdeljena_beseda = razdeli_besedo(beseda)
    vzorec = izpisi_vzorec(beseda)
    polje.config(text=' '.join(vzorec))
    pop_up_okence.destroy()

def spremeni_vzorec(crka):
    global stevec_napacnih
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
                          command = lambda: nova_igra(zakljucek))
            b.pack()
            stevec_napacnih = 0
    else:
        stevec_napacnih += 1
        if stevec_napacnih > 0:
            slika.create_oval(60, 320, 240, 500)
        if stevec_napacnih > 1:
            slika.create_line(150, 320, 150, 100)
        if stevec_napacnih > 2:
            slika.create_line(150, 100, 300, 100)
        if stevec_napacnih > 3:
            slika.create_line(300, 100, 300, 160)
        if stevec_napacnih > 4:
            slika.create_oval(280, 160, 320, 200)
        if stevec_napacnih > 5:
            slika.create_line(300, 200, 300, 280)
        if stevec_napacnih > 6:
            slika.create_line(300, 230, 320, 250)
        if stevec_napacnih > 7:
            slika.create_line(300, 230, 280, 250)
        if stevec_napacnih > 8:
            slika.create_line(300, 280, 320, 300)
        if stevec_napacnih > 9:
            slika.create_line(300, 280, 280, 300)
            slika.create_oval(280, 160, 320, 200, fill = 'red')
            stevec_napacnih = 0
            zakljucek = tk.Toplevel()
            zakljucek.title('KONEC IGRE!')
            poskusi = tk.Message(zakljucek, text='Izgubil si!')
            poskusi.pack()
            b = tk.Button(zakljucek, text='Nova igra',
                          command= lambda: nova_igra(zakljucek))
            b.pack()

okno = tk.Tk()
okno.title('Vislice')
polje = tk.Label(text=' '.join(vzorec))
polje.grid(row = 1, column = 1, columnspan = 20)
a = tk.Button(okno, text = 'A', command = lambda:spremeni_vzorec('A'))
a.grid(row = 2, column = 1, columnspan = 2, ipadx = 10.5)
b = tk.Button(okno, text = 'B', command = lambda:spremeni_vzorec('B'))
b.grid(row = 2, column = 3, columnspan = 2, ipadx = 10.5)
c = tk.Button(okno, text = 'C', command = lambda:spremeni_vzorec('C'))
c.grid(row = 2, column = 5, columnspan = 2, ipadx = 10.5)
č = tk.Button(okno, text = 'Č', command = lambda:spremeni_vzorec('Č'))
č.grid(row = 2, column = 7, columnspan = 2, ipadx = 10.5)
d = tk.Button(okno, text = 'D', command = lambda:spremeni_vzorec('D'))
d.grid(row = 2, column = 9, columnspan = 2, ipadx = 10.5)
e = tk.Button(okno, text = 'E', command = lambda:spremeni_vzorec('E'))
e.grid(row = 2, column = 11, columnspan = 2, ipadx = 10.5)
f = tk.Button(okno, text = 'F', command = lambda:spremeni_vzorec('F'))
f.grid(row = 2, column = 13, columnspan = 2, ipadx = 10.5)
g = tk.Button(okno, text = 'G', command = lambda:spremeni_vzorec('G'))
g.grid(row = 2, column = 15, columnspan = 2, ipadx = 10.5)
h = tk.Button(okno, text = 'H', command = lambda:spremeni_vzorec('H'))
h.grid(row = 2, column = 17, columnspan = 2, ipadx = 10.5)
i = tk.Button(okno, text = 'I', command = lambda:spremeni_vzorec('I'))
i.grid(row = 2, column = 19, columnspan = 2, ipadx = 10.5)
j = tk.Button(okno, text = 'J', command = lambda:spremeni_vzorec('J'))
j.grid(row = 3, column = 1, columnspan = 2, ipadx = 10.5)
k = tk.Button(okno, text = 'K', command = lambda:spremeni_vzorec('K'))
k.grid(row = 3, column = 3, columnspan = 2, ipadx = 10.5)
l = tk.Button(okno, text = 'L', command = lambda:spremeni_vzorec('L'))
l.grid(row = 3, column = 5, columnspan = 2, ipadx = 10.5)
m = tk.Button(okno, text = 'M', command = lambda:spremeni_vzorec('M'))
m.grid(row = 3, column = 7, columnspan = 2, ipadx = 9)
n = tk.Button(okno, text = 'N', command = lambda:spremeni_vzorec('N'))
n.grid(row = 3, column = 9, columnspan = 2, ipadx = 10)
o = tk.Button(okno, text = 'O', command = lambda:spremeni_vzorec('O'))
o.grid(row = 3, column = 11, columnspan = 2, ipadx = 10)
p = tk.Button(okno, text = 'P', command = lambda:spremeni_vzorec('P'))
p.grid(row = 3, column = 13, columnspan = 2, ipadx = 10.5)
r = tk.Button(okno, text = 'R', command = lambda:spremeni_vzorec('R'))
r.grid(row = 3, column = 15, columnspan = 2, ipadx = 10.5)
s = tk.Button(okno, text = 'S', command = lambda:spremeni_vzorec('S'))
s.grid(row = 3, column = 17, columnspan = 2, ipadx = 10.5)
š = tk.Button(okno, text = 'Š', command = lambda:spremeni_vzorec('Š'))
š.grid(row = 3, column = 19, columnspan = 2, ipadx = 10.5)
t = tk.Button(okno, text = 'T', command = lambda:spremeni_vzorec('T'))
t.grid(row = 4, column = 6, columnspan = 2, ipadx = 10.5)
u = tk.Button(okno, text = 'U', command = lambda:spremeni_vzorec('U'))
u.grid(row = 4, column = 8, columnspan = 2, ipadx = 10.5)
v = tk.Button(okno, text = 'V', command = lambda:spremeni_vzorec('V'))
v.grid(row = 4, column = 10, columnspan = 2, ipadx = 10.5)
z = tk.Button(okno, text = 'Z', command = lambda:spremeni_vzorec('Z'))
z.grid(row = 4, column = 12, columnspan = 2, ipadx = 10.5)
ž = tk.Button(okno, text = 'Ž', command = lambda:spremeni_vzorec('Ž'))
ž.grid(row = 4, column = 14, columnspan = 2, ipadx = 10.5)

slika = tk.Canvas(height=400, width=400, bd=1,
                  highlightthickness=1, relief='ridge')
slika.grid(row = 5, column = 1, columnspan = 20)


okno.mainloop()
