import random
import tkinter as tk

# Najprej naredim seznam besed iz datoteke, da se bo lahko beseda izbirala
def besede_v_seznam(ime_datoteke):
    seznam_besed = []
    with open(ime_datoteke, encoding='utf-8') as besede:
        for vrstica in besede:
            s2 = vrstica.strip()
            seznam_besed.append(s2)
    return seznam_besed

seznam_besed = besede_v_seznam('Besede.txt')

# Funkcija postavi igro na sredino zaslona in postavi pop-up okna na sredino
# igre
def center(okno, sirina, visina):
    ws = okno.winfo_screenwidth()
    hs = okno.winfo_screenheight()
    x = (ws/2) - (sirina/2)
    y = (hs/2) - (visina/2)
    okno.geometry('%dx%d+%d+%d' % (sirina, visina, x, y))
    okno.update_idletasks()

# Slovar črk rabimo za abecedo v grafičnem vmesniku, indeksi so liha števila,
# ker se je vsak stolpec širok dva stolpca, da je lahko slika večja
slovar_crk = {1:'A', 3:'B', 5:'C', 7:'Č', 9:'D', 11:'E', 13:'F', 15:'G',
                17:'H', 19:'I', 21:'J', 23:'K', 25:'L', 27:'M', 29:'N', 31:'O',
                33:'P', 35:'R', 37:'S', 39:'Š', 41:'T', 43:'U', 45:'V', 47:'Z',
                49:'Ž'}

# Na začetku nastavimo števca zmag in porazov, da lahko igralec ve koliko iger
# je že odigral.
zmage = 0
porazi = 0

class Vislice:

    # Nastavimo začetne spremenljivke
    def __init__(self):
        self.beseda = random.choice(seznam_besed)
        self.vzorec = self.izpisi_vzorec(self.beseda)
        self.razdeljena_beseda = self.razdeli_besedo(self.beseda)
        self.stevec_napacnih = 0
        self.okno = tk.Tk()
        center(self.okno, 400, 500)
        self.okno.title('Vislice')
        self.slika = tk.Canvas(self.okno, height=400, width=400, bd=1,
                    relief='ridge', bg = 'seashell')
        self.slika.grid(row = 5, column = 1, columnspan = 20)
        self.polje = tk.Label(text=' '.join(self.vzorec))
        self.polje.grid(row = 1, column = 1, columnspan = 20)
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
        self.polje.config(text=' '.join(self.vzorec))
        pop_up_okence.destroy()

    # Sestavimo samo abecedo s pomočjo slovarja, ki ga imamo napisanega na
    # začetku (ker je spremenljivki vedno ime a moramo namesto lambda: napisati
    # lambda i = i: da funkcijo prisilimo, da vsakič naredi novo spremenljivko)
    def abeceda(self):
        global slovar_crk
        for i in slovar_crk:
            if 1 <= i < 21:
                a = tk.Button(self.okno, text = slovar_crk[i],
                command = lambda i=i: self.spremeni_vzorec(slovar_crk[i]),
                bg = 'SlateGray1')
                a.grid(row = 2, column = i, columnspan = 2,
                sticky= 'w'+'e'+'n'+'s')
            if 21 <= i < 41:
                a = tk.Button(self.okno, text = slovar_crk[i],
                command = lambda i=i: self.spremeni_vzorec(slovar_crk[i]),
                bg = 'SlateGray2')
                a.grid(row = 3, column = i-20, columnspan = 2,
                sticky= 'w'+'e'+'n'+'s')
            if i >= 41:
                a = tk.Button(self.okno, text = slovar_crk[i],
                command = lambda i=i: self.spremeni_vzorec(slovar_crk[i]),
                bg = 'SlateGray3')
                a.grid(row = 4, column = i-35, columnspan = 2,
                sticky= 'w'+'e'+'n'+'s')

        # Dodamo funkcijo ki zažene grafični vmesnik
        self.okno.mainloop()

    # S pomočjo izpisane abecede dobimo črko, če je v dani besedi, potem mesto
    # na vzorcu zamenja črka, če ne se na platnu izriše del slike. Ko je slika
    # narisana je igre konec
    def spremeni_vzorec(self, crka):
        global zmage
        global porazi
        if crka in self.razdeljena_beseda:
            for i, value in enumerate(self.razdeljena_beseda):
                if value == str(crka):
                    self.vzorec[i] = value.replace('__', crka)
            self.polje.config(text=' '.join(self.vzorec))
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
                center(zakljucek, 130, 80)
        else:
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
                            porazi), anchor = 'center', width=30)
                poskusi.grid(row = 0, rowspan = 4, column = 1, columnspan = 3)
                nov_level = tk.Button(zakljucek, text='Nova igra',
                            command= lambda: self.nova_igra(zakljucek),
                            bg = 'medium sea green')
                nov_level.grid(row = 5, column = 1)
                konec_igre = tk.Button(zakljucek, text='Izhod',
                            command = lambda: self.okno.destroy(),
                            bg = 'tomato')
                konec_igre.grid(row = 5, column = 3, ipadx = 10)
                center(zakljucek, 210, 100)

# Na koncu še zaženemo program
Vislice()
