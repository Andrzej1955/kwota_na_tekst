# liczba_tekst_okieno
# Tworzy okno do wpisanoia i uzyskania ntejkstu kwoty

from tkinter import *
import re
import time

#==============================================================================
#POCZĄTEK - ZAMIANA

#przecinek = ""  #znak oddzielajacy część cakowita od części dziesiętnej
liczba = ""     #wczytana liczba
liczba_P = ''
format_gr = ''  #wybór formatu groszy
kwota_s = ''
kwota_ = ''
PRZECINEK = '.'
CYFRY = '0123456789'

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
    #zamiana '.' na '0'
    przecinek = liczba[-3]
    liczba = liczba.replace(przecinek,'0')
    print('liczba zamiana 1: ',liczba)

    plik = open("liczba.txt", "w")
    plik.write(liczba)
    plik.close()
    
    #Sprawdzenie długości części całkowitej liczby
    liczba_cc = liczba[:-3]    #część całkowita liczby
#    print('liczba_cc: ',liczba_cc)
    #utworzenie liczby o długości 15 znaków
    #dopełnienie liczby krótszej niż 15 znaków znakami "0" - po lewej stronie
#    liczba_c = ('0' * (15 - int((len(liczba))))) + liczba   #liczba cała 15 znaków
    liczba_c = ('0' * (15 - len(liczba))) + liczba   #liczba cała 15 znaków
    print('liczba_c zamiana 2: ',liczba_c)
    #=====================================================
    #Tworzenie [list] z częściami trójkowymi liczby
    #trojki = [mld, mln, tys, setk, gr] #tablica 3-znakowych sekwencji liczb
    #wstawienie liczby - całej 15-znakowej 'liczba_c'
    # - podzielonej na 3-znakowe sekwencje
    # - do tablicy 'trojki'

    #trojki = ['','','','',''] #tablica 3-znakowych sekwencji liczb

    trojki = [] #tablica 3-znakowych sekwencji liczb

    trojki = [(liczba_c[j:j+3]) for (j) in range(0,15,3)]

    print('trojki: ',trojki)

    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #trojki_s - zamiana tablicy 'trojki' na string
    #w celu zamiany wpowadzonej liczby na format ###.###.###.##0,00

    trojki_s = ''
    for s in range(5):
        trojki_s += trojki[s]+ '.'
    print('trojki_s: ',trojki_s)

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

#    try:
#        if int(liczba_cc) == 0:
#            slowa [12] = ''
#            slowa [13] = ''
#            slowa [14] = zero
#            slowa [15] = nazwy_j[3][3]
#    except ValueError:
#        liczba_P = ''
#        kontrola(liczba_P)

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
    '''Formatowanie wprowadzonej kwoty do obliczeń'''
    
    dl_liczba = len(liczba_P)   #długość liczba_P
    p = liczba_P.count('.')     #czy kropka dziesiętna jest w liczba_P

    print('dl_liczba: ',dl_liczba)
    print('p: ',p)

    d = None
    for i in range(dl_liczba):
        if liczba_P[i] == '.':
            d = i

    if p == 1:
        if d <= 12 and dl_liczba <= 15 and (dl_liczba - d) == 1:
            liczba_P = liczba_P + '00'
        if d <= 12 and dl_liczba <= 15 and (dl_liczba - d) == 2:
            liczba_P = liczba_P + '0'
        if d <= 12 and dl_liczba <= 15 and (dl_liczba - d) == 3:
            liczba_P = liczba_P
        if d <= 12 and dl_liczba <= 15 and (dl_liczba - d) >= 3:
            liczba_P = liczba_P[:d+1] + liczba_P[d+1:d+3]
        if d > 13:
            liczba_P = 'BŁĄD'
    else:
        if dl_liczba == 0:
            liczba_P = 'BŁĄD'
        elif 0 < dl_liczba <= 12:
            liczba_P = liczba_P + '.00'
        if dl_liczba > 12:
            liczba_P = 'BŁĄD'
    wynik = liczba_P
    return wynik

def liczba_F(kwota_):
    '''Zamiana wpowadzonej liczby na format księgowy ###.###.###.##0,00'''

    plik_1 = open("trojki_s.txt", "r")
    kwota_F = plik_1.read()
    plik_1.close()
    kwota_F = kwota_F[:19]

    if kwota_F[:17] == '000.000.000.000.0':
        kwota_F = '0.' + kwota_F[17:19]
    else:
        kwota_F1 = []
#        for i in range(19):
#            u = kwota_F[i]
#            kwota_F1.append(u)
        kwota_F1 = [(kwota_F[i]) for i in range(19)]
        print('kwota_F1 - liczba_F: ',kwota_F1)
        kwota_F = kwota_F1[:]
        m = 0
        while kwota_F[m] == '0' or kwota_F[m] == '.':
            m = 0
            del kwota_F[m]
        kwota_F = kwota_F[m:19]

        m=0
        u = ''
        d = len(kwota_F)
        while kwota_F[m]:
            u += kwota_F[m]
            m += 1
            if m == d:
                break
        u = u[:-4]+','+u[-2:]
        kwota_F = u

    return kwota_F
   
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
        #etykieta z instrukcją
        self.inst_lbl = Label(self, font = ('calibri', 11),
              text =
"======================================================================================================\n \
\t\t\t\t\tZAMIANA KWOTY NA TEKST\n\
\tPodaj kwotę w złotych z przedziału <0,  999.999.999.999,99> w formacie : ##### lub w formacie : ###.##\n\
\t\tskładającą się tylko ze znaków: \'0123456789.\' oraz wybierz format 'groszy'\n \
======================================================================================================", justify='left'
              ).grid(row = 0, column = 1, columnspan = 5, sticky = W) #rowspan = 1, columnspan = 5) #, sticky = W)


        # utwórz etykietę i pole znakowe służące do wpisania liczby
        self.wpisz_lbl = Label(self, font = ('calibri', 11),
              text = '   Wpisz kwotę:'
              ).grid(row = 9, column =2,sticky = W)#columnspan = 2

        sv = StringVar()
        self.liczba_P = Entry(self, justify = RIGHT, textvariable = sv)
        self.liczba_P.grid(row = 9, column = 2, columnspan = 2)#, sticky = W)#
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

#==============================================================================

        # utwórz etykietę z pytaniem o wybór formatu groszy
        self.wpisz_2_lbl = Label(self, font = ('calibri', 11),
              text = "Wybierz format groszy:"
              ).grid(row = 10, column = 1, columnspan = 3)#, sticky = W) #, rowspan = 1) #, columnspan = 5)  #, sticky = W)

#==============================================================================
        # utwórz zmienną, która ma reprezentować pojedynczy format groszy
        self.format_gr = StringVar()
        self.format_gr.set(None)
#        self.format_gr.set('1')

        # utwórz przycisk opcji do wyboru formatu groszy - tekstowego
        Radiobutton(self,
                    text = "zero groszy",
                    indicatoron = 0,
                    width = 22,
                    variable = self.format_gr,
                    value = "1",
                    pady = 2
                    ).grid(row = 11, column = 1)

        # utwórz przycisk opcji do wyboru dramatu
        Radiobutton(self,
                    text = "00 groszy",
                    indicatoron = 0,
                    width = 22,
                    variable = self.format_gr,
                    value = "2",
                    pady = 2
                    ).grid(row = 11, column = 2)

        # utwórz przycisk opcji do wyboru romansu
        Radiobutton(self,
                    text = "00/100",
                    indicatoron = 0,
                    width = 22,
                    variable = self.format_gr,
                    value = "3",
                    pady = 2
                    ).grid(row = 11, column = 3)

#==============================================================================

        # utwórz przycisk - Przycisk 'OK' - liczba na tekst
        self.wykonaj_2 = Button(self,
                                text = "OK",
                                font = ('calibri',13, 'underline'),
                                padx = 83,
                                pady = 20,
                                command = self.wpisz_1
                                )
        self.wykonaj_2.grid(row = 9, rowspan = 6, column = 5)#, sticky = W)	rowspan = 15, 

#==============================================================================

        # utwórz przycisk zamknięcia okna
        self.koniec_ost = Button(self,
                                 text = "KONIEC",
                                 font = ('calibri',13, 'underline'),
                                 padx = 35,
                                 command = root.destroy)
        self.koniec_ost.grid(row = 31, column = 1,columnspan = 5)#, sticky = W)

#==============================================================================
        # utwórz etykietę z pustą linią '0' -'' - lewa ramka
        self.linia = Label(self, font = ('Courier New', 5),
              text = "     "
              ).grid(row = 32, column = 0)

        # utwórz etykietę z linią '1' - '=================='
        self.linia = Label(self, font = ('Courier New', 5),
              text = "  ", justify='left'
              ).grid(row = 18, column = 1, columnspan = 5)

        # utwórz etykietę z pustą linią '2' '' - prawa rfamka
        self.linia = Label(self, font = ('Courier New', 5),
              text = "    "
              ).grid(row = 32, column = 4)

        # utwórz etykietę z pustą linią '2' '' - prawa rfamka
        self.linia = Label(self, font = ('Courier New', 5),
              text = "     "
              ).grid(row = 32, column = 6)

       # utwórz widżet Text do wyświetlenia komunikatu 'tekst kwoty' lub 'wpisz kwotę'
        self.kwota_txt = Text(self,  font = ('Calibri', 11),width = 100, height = 6, wrap = WORD, padx = 10, pady = 10)
        self.kwota_txt.grid(row = 29, column = 1 ,columnspan = 5)#, sticky = E)



        # utwórz etykietę z pustą linią '3' '=================='
        self.linia = Label(self, font = ('Courier New', 5),
              text = "", justify='left'
              ).grid(row = 30, column = 1)#, sticky = W) #rowspan = 1, columnspan = 5) #, sticky = W)

        # utwórz etykietę z pustą linią '4' '=================='
        self.linia = Label(self, font = ('Courier New', 5),
              text = "", justify='left'
              ).grid(row = 32, column = 1)#, sticky = W) #rowspan = 1, columnspan = 5) #, sticky = W)






#==============================================================================

    def validate_float(self,var):
        '''
        Sprawdzenie poprawności wprowadzenia liczby zmiennoprzecinkowej
        w polu "Entry":
            sv = StringVar()
            self.ac = Entry(self, .... , textvariable = sv)
          self.ac.grid(row = 3, column = 9)
          sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var))
        '''
        validate_old_value = ''
        new_value = var.get()
        try:
            new_value == float(new_value) 
            validate_old_value = new_value
        except:
            var.set(validate_old_value)    


    def wpisz_1(self):
        """ Wyświetl komunikat zależny od od stanu przycisku 'OK_2'. """
        liczba_P = self.liczba_P.get()
        format_gr = self.format_gr.get()
        liczba = kontrola(liczba_P)
        print('liczba wpisz_1: ',liczba)
        napis = liczba
        if napis == 'BŁĄD':
            napis = 'Niewłaściwy format wprowadzonej kwoty!\n Wprowadż właściwą kwotę.'
            self.kwota_txt.delete(0.0, END)
            self.kwota_txt.insert(0.0, 'Kwota podana:\n' + liczba_P + '\n\n'+ napis)
            first = '0'
            last = len(liczba_P)
            self.liczba_P.delete(first,last)
            self.format_gr.set(None)
            #liczba = ''
            #pass
        format_gr = self.format_gr.get()
        kwota_s = zamiana(liczba,format_gr)

        kwota_C = liczba_F(kwota_)

        linie = []
        try:
            with open("kwota_slownie.txt", "r") as lin:  # odczytywanie linia po linii do listy
                linie = lin.readlines()
#                for linia in linie:
#                    print(linia.strip())
        except FileNotFoundError:
            with open("kwota_slownie.txt", "a") as plik:
                plik.close()
        if len(linie) > 50:
            del linie[:10]
#            print('\nBIG BANG\n')
        with open("kwota_slownie.txt", "w") as lin:  # zapis linii
            lin.writelines(linie[:])
#            lin.close()

        with open("kwota_slownie.txt", "a") as plik:
#        plik = open("kwota_slownie.txt", "a")
            kwoty = ('\nKwota podana księgowo:\n',kwota_C,' zł','\nKwota słownie:\n',kwota_s,'\n')
            plik.writelines(kwoty)
#            plik.close()

        first = '0'
        last = len(liczba_P)
        self.liczba_P.delete(first,last)

        napis_1 = '\
Kwota podana: '
        napis_2 = ' zł\t\t\t\t\t\
Kwota sformatowana księgowo: '
        napis_3 = ' zł\n\
Kwota słownie:\n'
        napis_4 = '\n=====================\n\
Kwota słownie została zapisana do pliku "kwota_slownie.txt"'
        napis = napis_1 + liczba_P + napis_2 + kwota_C + napis_3 + kwota_s + napis_4

        self.kwota_txt.delete(0.0, END)
        self.kwota_txt.insert(0.0, napis)
        self.format_gr.set(None)

#==============================================================================

# część główna
root = Tk()
root.title('Zamiana liczby na tekst')
#root.geometry('550x630')
app = Apka(root)
root.mainloop()
