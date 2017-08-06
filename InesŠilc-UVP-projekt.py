import random
import tkinter as tk

# Najprej naredim seznam besed iz datoteke, da se bo lahko beseda izbirala
def besede_v_seznam(ime_datoteke):
    seznam_besed = []
    with open(ime_datoteke, encoding='utf-8') as besede:
        for vrstica in besede:
            beseda = vrstica.strip()
            seznam_besed.append(beseda)
    return seznam_besed

seznam_besed = besede_v_seznam('Besede.txt')

# Na začetku nastavimo števca zmag in porazov, da lahko igralec ve koliko iger
# je že odigral.
zmage = 0
porazi = 0

class Vislice:

    def __init__(self):
        self.beseda = random.choice(seznam_besed)
        self.vzorec = self.izpisi_vzorec(self.beseda)
        self.razdeljena_beseda = self.razdeli_besedo(self.beseda)
        self.stevec_napacnih = 0
        self.okno = tk.Tk()
        self.okno.title('Vislice')
        self.slika = tk.Canvas(self.okno, height=400, width=400, bd = 1,
                    relief='sunken')
        self.slika.grid(row = 5, column = 1, columnspan = 20)
        self.polje = tk.Label(text='  '.join(self.vzorec))
        self.polje.grid(row = 1, column = 1, columnspan = 20)
        self.slovar_crk = ['A', 'B', 'C', 'Č', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S','Š',
                        'T', 'U', 'V', 'Z', 'Ž']
        self.seznam = []
        self.abeceda = self.abeceda()

    # Besedo spremenimo v vzorec oblike '__ __ ... __ __' za izpisovanje na
    # vmesniku
    def izpisi_vzorec(self, beseda):
        vzorec = []
        for x in range(len(self.beseda)):
            vzorec.append('__')
        return vzorec

    # Besedo razdelimo na črke, da se bodo le te lahko menjale pri spremembi
    # vzorca
    def razdeli_besedo(self, beseda):
        razdeljena_beseda = []
        for x in self.beseda:
            razdeljena_beseda.append(x)
        return razdeljena_beseda

    # Pri vsaki novi igri se slika zbriše, izbere nova beseda, na novo definira
    # vzorec in polje na katerem je vzorec izpisan
    def nova_igra(self, pop_up_okence):
        self.slika.delete("all")
        self.beseda = random.choice(seznam_besed)
        self.razdeljena_beseda = self.razdeli_besedo(self.beseda)
        self.vzorec = self.izpisi_vzorec(self.beseda)
        self.polje.config(text='  '.join(self.vzorec))
        pop_up_okence.destroy()
        self.seznam = []
        self.abeceda()

    def abeceda(self):
        a = tk.Button(self.okno, text = 'A',
            command = lambda:self.spremeni_vzorec('A'), bg = 'SlateGray1')
        a.grid(row = 2, column = 1, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(a)
        b = tk.Button(self.okno, text = 'B',
            command = lambda:self.spremeni_vzorec('B'), bg = 'SlateGray1')
        b.grid(row = 2, column = 3, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(b)
        c = tk.Button(self.okno, text = 'C',
            command = lambda:self.spremeni_vzorec('C'), bg = 'SlateGray1')
        c.grid(row = 2, column = 5, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(c)
        č = tk.Button(self.okno, text = 'Č',
            command = lambda:self.spremeni_vzorec('Č'), bg = 'SlateGray1')
        č.grid(row = 2, column = 7, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(č)
        d = tk.Button(self.okno, text = 'D',
            command = lambda:self.spremeni_vzorec('D'), bg = 'SlateGray1')
        d.grid(row = 2, column = 9, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(d)
        e = tk.Button(self.okno, text = 'E',
            command = lambda:self.spremeni_vzorec('E'), bg = 'SlateGray1')
        e.grid(row = 2, column = 11, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(e)
        f = tk.Button(self.okno, text = 'F',
            command = lambda:self.spremeni_vzorec('F'), bg = 'SlateGray1')
        f.grid(row = 2, column = 13, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(f)
        g = tk.Button(self.okno, text = 'G',
            command = lambda:self.spremeni_vzorec('G'), bg = 'SlateGray1')
        g.grid(row = 2, column = 15, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(g)
        h = tk.Button(self.okno, text = 'H',
            command = lambda:self.spremeni_vzorec('H'), bg = 'SlateGray1')
        h.grid(row = 2, column = 17, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(h)
        i = tk.Button(self.okno, text = 'I',
            command = lambda:self.spremeni_vzorec('I'), bg = 'SlateGray1')
        i.grid(row = 2, column = 19, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(i)
        j = tk.Button(self.okno, text = 'J',
            command = lambda:self.spremeni_vzorec('J'), bg = 'SlateGray2')
        j.grid(row = 3, column = 1, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(j)
        k = tk.Button(self.okno, text = 'K',
            command = lambda:self.spremeni_vzorec('K'), bg = 'SlateGray2')
        k.grid(row = 3, column = 3, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(k)
        l = tk.Button(self.okno, text = 'L',
            command = lambda:self.spremeni_vzorec('L'), bg = 'SlateGray2')
        l.grid(row = 3, column = 5, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(l)
        m = tk.Button(self.okno, text = 'M',
            command = lambda:self.spremeni_vzorec('M'), bg = 'SlateGray2')
        m.grid(row = 3, column = 7, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(m)
        n = tk.Button(self.okno, text = 'N',
            command = lambda:self.spremeni_vzorec('N'), bg = 'SlateGray2')
        n.grid(row = 3, column = 9, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(n)
        o = tk.Button(self.okno, text = 'O',
            command = lambda:self.spremeni_vzorec('O'), bg = 'SlateGray2')
        o.grid(row = 3, column = 11, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(o)
        p = tk.Button(self.okno, text = 'P',
            command = lambda:self.spremeni_vzorec('P'), bg = 'SlateGray2')
        p.grid(row = 3, column = 13, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(p)
        r = tk.Button(self.okno, text = 'R',
            command = lambda:self.spremeni_vzorec('R'), bg = 'SlateGray2')
        r.grid(row = 3, column = 15, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(r)
        s = tk.Button(self.okno, text = 'S',
            command = lambda:self.spremeni_vzorec('S'), bg = 'SlateGray2')
        s.grid(row = 3, column = 17, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(s)
        š = tk.Button(self.okno, text = 'Š',
        command = lambda:self.spremeni_vzorec('Š'), bg = 'SlateGray2')
        š.grid(row = 3, column = 19, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(š)
        t = tk.Button(self.okno, text = 'T',
            command = lambda:self.spremeni_vzorec('T'), bg = 'SlateGray3')
        t.grid(row = 4, column = 6, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(t)
        u = tk.Button(self.okno, text = 'U',
            command = lambda:self.spremeni_vzorec('U'), bg = 'SlateGray3')
        u.grid(row = 4, column = 8, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(u)
        v = tk.Button(self.okno, text = 'V',
            command = lambda:self.spremeni_vzorec('V'), bg = 'SlateGray3')
        v.grid(row = 4, column = 10, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(v)
        z = tk.Button(self.okno, text = 'Z',
            command = lambda:self.spremeni_vzorec('Z'), bg = 'SlateGray3')
        z.grid(row = 4, column = 12, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(z)
        ž = tk.Button(self.okno, text = 'Ž',
            command = lambda:self.spremeni_vzorec('Ž'), bg = 'SlateGray3')
        ž.grid(row = 4, column = 14, columnspan = 2, sticky = 'w'+'e'+'n'+'s')
        self.seznam.append(ž)

        self.okno.mainloop()

    # S pomočjo izpisane abecede dobimo črko, če je v dani besedi, potem mesto
    # na vzorcu zamenja črka, če ne se na platnu izriše del slike. Ko je slika
    # narisana je igre konec
    def spremeni_vzorec(self, crka):
        global zmage
        global porazi
        if crka in self.razdeljena_beseda:
            self.seznam[self.slovar_crk.index(crka)].config(bg = 'gray91',
                                                            state = 'disabled')
            for i, value in enumerate(self.razdeljena_beseda):
                if value == str(crka):
                    self.vzorec[i] = value.replace('__', crka)
            self.polje.config(text='  '.join(self.vzorec))
            if self.razdeljena_beseda == self.vzorec:
                self.stevec_napacnih = 0
                zmage += 1
                # Ko se vzorec in beseda ujemata pomeni, da je igralec pravilno
                # uganil besedo, zato se število zmag poveča za 1 in izpiše se
                # okno, na katerem je podano število zmag in porazov, ter
                # opciji da igralec nadaljuje ali zapusti igro. Če se odloči
                # nadaljevati se pokliče funkcija nova_igra, če pa se odloči
                # igro zapustiti se izvede funkcija, ki zaključi program.
                zakljucek = tk.Toplevel()
                zakljucek.title('KONEC IGRE!')
                poskusi = tk.Label(zakljucek, text=('Zmagal si!\n'+
                            'Število zmag: {}\n'+
                            'Število porazov: {}').format(zmage, porazi),
                            anchor = 'center', width=20)
                poskusi.grid(row = 0, rowspan = 3, column = 1, columnspan = 3)
                nov_level = tk.Button(zakljucek, text='Nova igra',
                            command= lambda: self.nova_igra(zakljucek),
                            bg = 'medium sea green')
                nov_level.grid(row = 3, column = 1)
                konec_igre = tk.Button(zakljucek, text='Izhod',
                            command = lambda: self.okno.destroy(),
                            bg = 'tomato')
                konec_igre.grid(row = 3, column = 3, ipadx = 10)
        else:
            self.seznam[self.slovar_crk.index(crka)].config(bg = 'gray91',
                                                            state = 'disabled')
            # Če se vnešena črka ne ujema z nobeno črko v besedi se začne
            # izrisovati slika. Igralec ima na voljo 9 napačnih vnosov, pri
            # desetem je igra izgubljena, prikaže se podobno okno kot pri
            # zmagovalcu, le da je tu dodana še pravilna beseda
            self.stevec_napacnih += 1
            if self.stevec_napacnih > 0:
                self.slika.create_oval(60, 320, 240, 500)
            if self.stevec_napacnih > 1:
                self.slika.create_line(150, 320, 150, 100)
            if self.stevec_napacnih > 2:
                self.slika.create_line(150, 100, 300, 100)
            if self.stevec_napacnih > 3:
                self.slika.create_line(300, 100, 300, 160)
            if self.stevec_napacnih > 4:
                self.slika.create_oval(280, 160, 320, 200)
            if self.stevec_napacnih > 5:
                self.slika.create_line(300, 200, 300, 280)
            if self.stevec_napacnih > 6:
                self.slika.create_line(300, 230, 320, 250)
            if self.stevec_napacnih > 7:
                self.slika.create_line(300, 230, 280, 250)
            if self.stevec_napacnih > 8:
                self.slika.create_line(300, 280, 320, 300)
            if self.stevec_napacnih > 9:
                porazi += 1
                self.slika.create_line(300, 280, 280, 300)
                self.slika.create_line(290, 190, 310, 190)
                self.slika.create_line(290, 170, 295, 180)
                self.slika.create_line(295, 170, 290, 180)
                self.slika.create_line(305, 170, 310, 180)
                self.slika.create_line(310, 170, 305, 180)
                self.stevec_napacnih = 0
                zakljucek = tk.Toplevel()
                zakljucek.title('KONEC IGRE!')
                poskusi = tk.Label(zakljucek, text=('Izgubil si!\n'+
                            'Iskana beseda: {}\n'+
                            'Število zmag: {}\n'+
                            'Število porazov: {}').format(self.beseda, zmage,
                            porazi), anchor = 'center', width = 30)
                poskusi.grid(row = 0, rowspan = 4, column = 1, columnspan = 3)
                nov_level = tk.Button(zakljucek, text='Nova igra',
                            command= lambda: self.nova_igra(zakljucek),
                            bg = 'medium sea green')
                nov_level.grid(row = 5, column = 1)
                konec_igre = tk.Button(zakljucek, text='Izhod',
                            command = lambda: self.okno.destroy(),
                            bg = 'tomato')
                konec_igre.grid(row = 5, column = 3, ipadx = 10)

Vislice()
