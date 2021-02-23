# liczba_tekst_okieno
# Tworzy okno do wpisanoia i uzyskania ntejkstu kwoty

from tkinter import *
import re

#==============================================================================
#POCZĄTEK - ZAMIANA

#przecinek = ""  #znak oddzielajacy część cakowita od części dziesiętnej
liczba = ""     #wczytana liczba
liczba_P = ''
format_gr = ''  #wybór formatu groszy
kwota_s = ''
kwota_ = ''
#wynik = ''
#filepath = ''      
#=================================================
#Tablice ze słowami
zero = ('zero')
jednostki = ('','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć')
jednostki_1 = ('','jedenaście','dwanaście','trzynaście','czternaście','piętnaście','szesnaście','siedemnaście','osiemnaście','dziewięnaście')
dziesiatki = ('','dziesięć','dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt')
setki = ('','sto','dwieście','trzysta','czterysta','pięćset','sześćset','siedemset','osiemset','dziewięćset')
nazwy_j = (('','miliard','miliardy','miliardów'),
           ('','milion','miliony','milionów'),
           ('','tysiąc','tysiące','tysięcy'),
           ('','złoty','złote','złotych'),
           ('groszy','grosz','grosze','groszy'))

#=================================================

#==================================================
#ZAMIANA CYFR NA SŁOWA

def zamiana(liczba,format_gr):
    '''ZAMIANA CYFR NA SŁOWA'''
    #zamiana '.,' na '0'
    przecinek = liczba[-3]
    liczba = liczba.replace(przecinek,'0')

    #liczba = liczba.replace('\,','0')
    liczba = liczba.replace('.','')
    liczba = liczba.replace(',','')

    plik = open("liczba.txt", "w")
    plik.write(liczba)
    plik.close()
    
    #Sprawdzenie długości części całkowitej liczby
    liczba_cc = liczba[:-3]    #część całkowita liczby
    #utworzenie liczby o długości 15 znaków
    #dopełnienie liczby krótszej niż 15 znaków znakami "0" - po lewej stronie
    liczba_c = ('0' * (15 - int((len(liczba))))) + liczba   #liczba cała 15 znaków

    #=====================================================
    #Tworzenie [list] z częściami trójkowymi liczby
    #trojki = [mld, mln, tys, setk, gr] #tablica 3-znakowych sekwencji liczb
    #wstawienie liczby - całej 15-znakowej 'liczba_c'
    # - podzielonej na 3-znakowe sekwencje
    # - do tablicy 'trojki'

    #trojki = ['','','','',''] #tablica 3-znakowych sekwencji liczb
    trojki = [] #tablica 3-znakowych sekwencji liczb

    i = 0
    j = 0
    liczba_t = ''

    for i in range(5):
        liczba_t = liczba_c[j:j+3]
        trojki.insert(i, liczba_t)
        i +=1
        j += 3
    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #trojki_s - zamiana tablicy 'trojki' na string
    #w celu zamiany wpowadzonej liczby na format ###.###.###.##0,00


    trojki_s = ''
    s = 0
    for s in range(5):
        trojki_s += trojki[s]
        if trojki[s]:
            trojki_s += '.'
        else:
            trojki_s += ''
        s += 1

    plik = open("trojki_s.txt", "w")
    plik.write(trojki_s)
    plik.close()

    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    #=============================================
    #tablica do zapisu słów z przekształcenia poszczególnych cyfr wpisanej liczby
    slowa = []
    #===========================================================
    #PĘTLA GŁÓWNA - cyfry na słowa

    n = 0
    for k in range(5):
        slowa_0 = setki [int(trojki[k][0])]
        slowa.insert(n, slowa_0)

        if int(trojki [k][1:3]) >= 11 and int(trojki[k][1:3]) <= 19:
            slowa_1 = jednostki_1[int(trojki [k][2])]
            slowa_2 = ''
        else:
            slowa_1 = dziesiatki [int(trojki [k][1])]
            slowa_2 = jednostki [int(trojki [k][2])]
        slowa.insert(n+1, slowa_1)
        slowa.insert(n+2, slowa_2)

    # określenie sekwencji - słowo 'miliard/y/ów','milion/y/ów','tysiąc/e/ęcy','złoty/e/ych','grosz/e/y'
        if int(trojki[k]) == 0:
            slowa_s = nazwy_j[k][0]
        elif int(trojki[k]) == 1:
            slowa_s = nazwy_j[k][1]
        elif int(trojki[k][1:3]) >= 5 and int(trojki[k][1:3]) <= 21:
            slowa_s = nazwy_j[k][3]
        elif int(trojki[k][2]) >= 2 and int(trojki[k][2]) <= 4:
            slowa_s = nazwy_j[k][2]
        else:
            slowa_s = nazwy_j[k][3]

        slowa.insert(n+3, slowa_s)
        n += 4

    #CAŁA LICZBA 0,00 - (część całkowita) - słowo: 'zero'

    if int(liczba_cc) == 0:
        slowa [12] = ''
        slowa [13] = ''
        slowa [14] = zero
        slowa [15] = nazwy_j[3][3]

    #GROSZE - ,00 - słowo zero ({16} = ',')
    slowa [16] = ''

    if int(trojki[4]) == 0:
        slowa [17] = ''
        slowa [18] = zero

    if format_gr == '2':    #format '00 groszy'
        slowa [17] = ''
        slowa [18] = liczba[-2:]
        
    if format_gr == '3':    #format '00/100'
        slowa [17] = ''
        slowa [18] = ''
        slowa [19] = liczba[-2:]+'/100'

    #===========================================================
    #kwota słownie po usunięciu zbędnych znaków
    kwota_s = ''
    for m in range(20):
        kwota_s += slowa[m]
        if slowa[m]:
            kwota_s += ' '
        else:
            kwota_s += ''
        m += 1

    return kwota_s
    #KONIEC ZAMIANA
    #==========================================

def kontrola(liczba_P):
    #liczba = self.liczba_P.get()     #wczytywana liczba
    liczba = liczba_P
    pat = re.compile(r'[*]')    #zmienna 're' do sprawdzenia prawidłowosci wczytanej liczby
    #sprawdzenie czy znaki liczby są prawidłowe - wyrażenie regex
    pat = re.compile(r'^[0-9]{0,3}[.,]?[0-9]{0,3}[.,]?[0-9]{0,3}[.,]?[0-9]{0,2}[0-9][.,][0-9]{2}$')
    if not pat.match(liczba):
        wynik = 'Niewłaściwy format wprowadzonej kwoty!\n Wprowadż kwotę.'
    else:
        wynik = liczba
    return wynik

def liczba_F(kwota_):
    '''Zamiana wpowadzonej liczby na format ###.###.###.##0,00'''

    plik_1 = open("trojki_s.txt", "r")
    kwota_ = plik_1.read()
    plik_1.close()
    kwota_ = kwota_[:19]
    C = '123456789'
    m = 0
    if kwota_ == '000.000.000.000.000':
            kwota_ = '0,00'
    else:
        while kwota_[m] not in C:
            m += 1
        kwota_ = kwota_[m:19]
        kwota_ = kwota_[:-4]+','+kwota_[-2:]
    return kwota_
   
#==============================================================================
#POCZĄTEK OKNA

class Apka(Frame):
    """ Aplikacja z GUI, która zamienia liczbę - cyfry na liczbę - tekst. """
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Apka, self).__init__(master)  
        self.grid()
        self.create_widgets()

#==============================================================================

    def create_widgets(self):
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez
        użytkownika i wyświetlenia wyniku.
        """
        # utwórz etykietę z instrukcją
        self.inst_lbl = Label(self, font = ('calibri', 11),
              text =
"=================================================================\n \
\t\t      ZAMIANA LICZB NA TEKST\n\
\n\
 Podaj kwotę w złotych z przedziału <0,  999.999.999.999,99>\n \
 w formacie : ##.##0,00 (####0,00) lub w formacie : ##,##0.00 (####0.00)\n \
 i składającą się tylko ze znaków: \'0123456789.,\'\n \
 oraz wybierz format 'groszy'\n \
=================================================================", justify='left'
              ).grid(row = 0, column = 1, rowspan = 8, columnspan = 8, sticky = W) #rowspan = 1, columnspan = 5) #, sticky = W)


#==============================================================================


        # utwórz etykietę i pole znakowe służące do wpisania liczby
        self.wpisz_lbl = Label(self, font = ('calibri', 11),
              text = 'Wpisz kwotę:'
              ).grid(row = 9, column =1)#, sticky = W)
        self.liczba_P = Entry(self, justify = RIGHT)
        self.liczba_P.grid(row = 10, column = 1)#, sticky = W)#


#==============================================================================

        # utwórz etykietę z pytaniem o wybór formatu groszy
        self.wpisz_2_lbl = Label(self, font = ('calibri', 11),
              text = "i\nwybierz format groszy:"
              ).grid(row = 13, column = 1)#, sticky = W) #, rowspan = 1) #, columnspan = 5)  #, sticky = W)

#==============================================================================
        # utwórz zmienną, która ma reprezentować pojedynczy format groszy - (PĘTLA)
#        self.format_gr = StringVar()
        #self.format_gr.set(None)
#        self.format_gr.set('1')

        # utwórz przyciski opcji do wyboru formatu groszy
#        formaty_groszy = ['           zero groszy','           99 groszy','           99/100                 ']
#        f = 1
#        column = 0
#        for format in formaty_groszy:
#            Radiobutton(self,
#                        variable = self.format_gr,
#                        text = format,
#                        value = f
#                        ).grid(row = 14, column = column)#, sticky = W)
#            column += 1
#            f += 1


#==============================================================================
#==============================================================================
        # utwórz zmienną, która ma reprezentować pojedynczy format groszy
        self.format_gr = StringVar()
        self.format_gr.set(None)
#        self.format_gr.set('1')

        # utwórz przycisk opcji do wyboru formatu groszy - tekstowego
        Radiobutton(self,
                    text = "zero groszy",
                    variable = self.format_gr,
                    value = "1",
                    command = self.wpisz_1
                    ).grid(row = 14, column = 1, sticky = W)

        # utwórz przycisk opcji do wyboru dramatu
        Radiobutton(self,
                    text = "99 groszy",
                    variable = self.format_gr,
                    value = "2",
                    command = self.wpisz_1
                    ).grid(row = 14, column = 1)#, sticky = W)

        # utwórz przycisk opcji do wyboru romansu
        Radiobutton(self,
                    text = "99/100",
                    variable = self.format_gr,
                    value = "3",
                    command = self.wpisz_1
                    ).grid(row = 14, column = 1, sticky = E)

#==============================================================================

        # utwórz przycisk - Przycisk 'OK' - liczba na tekst
#        self.wykonaj_2 = Button(self,
#                                text = "OK",
#                                font = ('calibri',13, 'underline'),
#                                padx = 50,
#                                command = self.wpisz_1)
#        self.wykonaj_2.grid(row = 16, column = 1)#, sticky = W)	


#==============================================================================

        # utwórz przycisk zamknięcia okna
        self.koniec_ost = Button(self,
                                 text = "KONIEC",
                                 font = ('calibri',13, 'underline'),
                                 padx = 35,
                                 command = root.destroy)
        self.koniec_ost.grid(row = 31, column = 1)#, sticky = W)

#==============================================================================
        # utwórz etykietę z pustą linią '0' -'' - lewa ramka
        self.linia = Label(self, font = ('calibri', 11),
              text = "     "
              ).grid(row = 18, column = 0)

        # utwórz etykietę z linią '1' - '=================='
        self.linia = Label(self, font = ('calibri', 11),
              text = "==================================================================", justify='left'
              ).grid(row = 18, column = 1)

        # utwórz etykietę z pustą linią '2' '' - prawa rfamka
        self.linia = Label(self, font = ('calibri', 11),
              text = "     "
              ).grid(row = 18, column = 2)

#==============================================================================
       # utwórz widżet Text do wyświetlenia komunikatu 'OK' lub 'C'
        #self.kwota_P = Text(self, width = 20, height = 1)#, wrap = WORD)
        #self.kwota_P.grid(row = 19, column = 1)#, sticky = W)
#==============================================================================




       # utwórz widżet Text do wyświetlenia komunikatu 'tekst kwoty' lub 'wpisz kwotę'
        self.kwota_txt = Text(self, width = 55, height = 16, wrap = WORD, padx = 10, pady = 10)
        self.kwota_txt.grid(row = 29, column = 1)#, sticky = E)

        # utwórz etykietę z pustą linią '3' '=================='
        self.linia = Label(self, font = ('calibri', 11),
              text = "", justify='left'
              ).grid(row = 30, column = 1)#, sticky = W) #rowspan = 1, columnspan = 5) #, sticky = W)

        # utwórz etykietę z pustą linią '4' '=================='
        self.linia = Label(self, font = ('calibri', 11),
              text = "", justify='left'
              ).grid(row = 32, column = 1)#, sticky = W) #rowspan = 1, columnspan = 5) #, sticky = W)

#==============================================================================

    def wpisz_1(self):
        """ Wyświetl komunikat zależny od od stanu przycisku 'OK_2'. """
        liczba_P= self.liczba_P.get()
        format_gr = self.format_gr.get()
        liczba = kontrola(liczba_P)
        napis = liczba
        if napis == 'Niewłaściwy format wprowadzonej kwoty!\n Wprowadż kwotę.':
            self.kwota_txt.delete(0.0, END)
            self.kwota_txt.insert(0.0, liczba_P + '\n\n'+ napis)
            first = '0'
            last = len(liczba)
            self.liczba_P.delete(first,last)
        kwota_s = zamiana(liczba,format_gr)
        kwota_C = liczba_F(kwota_)
        plik = open("kwota_slownie.txt", "a")
        kwoty = ('\nKwota podana cyfrowo:\n',kwota_C,' zł','\nKwota słownie:\n',kwota_s,'\n')
        plik.writelines(kwoty)
        plik.close()

        first = '0'
        last = len(liczba)
        self.liczba_P.delete(first,last)

        napis_1 = '\
Kwota podana:\n'
        napis_2 = ' zł\n\n\
Kwota sformatowana cyfrowo:\n'
        napis_3 = ' zł\n\n\
Kwota słownie:\n'
        napis_4 = '\n=====================================================\n\
Kwota słownie została zapisana do pliku\n\
"kwota_slownie.txt"\n\
====================================================='
        napis = napis_1 + liczba_P + napis_2 + kwota_C + napis_3 + kwota_s + napis_4

        self.kwota_txt.delete(0.0, END)
        self.kwota_txt.insert(0.0, napis)

#==============================================================================

# część główna
root = Tk()
root.title('Zamiana liczby na tekst')
#root.geometry('550x630')
app = Apka(root)
root.mainloop()
