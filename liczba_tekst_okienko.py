# liczba_tekst_okieno
# Tworzy okno do wpisanoia i uzyskania ntejkstu kwoty

from tkinter import *
from src.libs import openFile
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

   
#==============================================================================
#POCZĄTEK OKNA

class Apka(Frame):
    """ Aplikacja z GUI, która zamienia liczbę - cyfry na liczbę - tekst. """
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Apka, self).__init__(master)  
        self.grid()
        self.create_widgets()
#        self.master.geometry('+800+15')
        self.center()      # wyśrodkuj

    def center(self):
        self.update()
        # szerokość / wysokość okna
        wx = self.winfo_width()
        wy = self.winfo_height()
        # szerokość wysokość ekranu
        sx = self.winfo_screenwidth()
        sy = self.winfo_screenheight()
        # środek ekranu przesunięty o 
        x = (sx - wx) // 2 # połowę szerokośi
        y = (sy - wy) // 2 # połowę wysokości

#        self.master.geometry("{}x{}+{}+{}".format(wx, wy, x, y))
        self.master.geometry("{}x{}+{}+30".format(wx, wy, x))#, y))

#==============================================================================

    def create_widgets(self):
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez
        użytkownika i wyświetlenia wyniku.
        """
        #etykieta z instrukcją
        self.inst_lbl = Label(self, font = ('calibri', 11),
              text =
"=============================================================================\
====================================\n \
\t\t\t\t\tZAMIANA KWOTY NA TEKST\n\
\tPodaj kwotę w złotych z przedziału <0,  999.999.999.999,99> w formacie : \
##### lub w formacie : ###.##\n\
\t\tskładającą się tylko ze znaków: \'0123456789.\' oraz wybierz format 'groszy'\n \
=============================================================================\
====================================", justify='left'
              ).grid(row = 0, column = 1, columnspan = 5, sticky = W) #rowspan = 1, columnspan = 5) #, sticky = W)


        # utwórz etykietę i pole znakowe służące do wpisania liczby
        self.wpisz_lbl = Label(self, font = ('calibri', 11),
              text = ' Wpisz kwotę:'
              ).grid(row = 9, column =1,sticky = W)#columnspan = 2

        sv = StringVar()
        self.liczba_P = Entry(self, justify = RIGHT, textvariable = sv)
        self.liczba_P.grid(row = 9, column = 1, columnspan = 2)#, sticky = W)#
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

#==============================================================================

        # utwórz etykietę z pytaniem o wybór formatu groszy
        self.wpisz_2_lbl = Label(self, font = ('calibri', 11),
              text = ' Domyślny format groszy: "zero zero groszy".'
              ).grid(row = 10, column = 1, columnspan = 3, sticky = W) #, rowspan = 1) #, columnspan = 5)  #, sticky = W)

#==============================================================================

        # utwórz etykietę z pytaniem o wybór formatu groszy
        self.wpisz_2_lbl = Label(self, font = ('calibri', 11),
              text = " Inne formaty groszy (wybierz):"
              ).grid(row = 11, column = 1, sticky = W) #, rowspan = 1) #, columnspan = 5)  #, sticky = W)

#==============================================================================

        # utwórz etykietę z pytaniem o wybór formatu groszy
#        self.wpisz_2_lbl = Label(self, font = ('calibri', 11),
#              text = "Wybierz format groszy:"
#              ).grid(row = 11, column = 1, sticky = W) #, rowspan = 1) #, columnspan = 5)  #, sticky = W)

#==============================================================================
        # utwórz zmienną, która ma reprezentować pojedynczy format groszy
        self.format_gr = StringVar()
        self.format_gr.set(None)
#        self.format_gr.set('1')

        # utwórz przycisk opcji do wyboru formatu groszy - tekstowego
#        Radiobutton(self,
#                    text = "zero groszy",
#                    indicatoron = 0,
#                    width = 22,
#                    variable = self.format_gr,
#                    value = "1",
#                    pady = 2
#                    ).grid(row = 10, column = 1)

        # utwórz przycisk opcji do wyboru dramatu
        Radiobutton(self,
                    text = "00 groszy",
                    indicatoron = 0,
                    width = 19,
                    variable = self.format_gr,
                    value = "2",
                    pady = 2
                    ).grid(row = 11, column = 2)

        # utwórz przycisk opcji do wyboru romansu
        Radiobutton(self,
                    text = "00/100",
                    indicatoron = 0,
                    width = 19,
                    variable = self.format_gr,
                    value = "3",
                    pady = 2
                    ).grid(row = 11, column = 3)

#==============================================================================

        # utwórz przycisk - Przycisk 'OK' - liczba na tekst
        self.wykonaj_2 = Button(self,
                                text = "OK",
                                font = ('calibri',13, 'underline'),
                                padx = 115,
                                pady = 20,
                                command = self.main
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

        # utwórz etykietę z pustą linią '2' '' - środek
        self.linia = Label(self, font = ('Courier New', 5),
              text = "   "
              ).grid(row = 32, column = 4)

        # utwórz etykietę z pustą linią '2' '' - prawa ramka
        self.linia = Label(self, font = ('Courier New', 5),
              text = "     "
              ).grid(row = 32, column = 6)

       # utwórz widżet Text do wyświetlenia komunikatu 'tekst kwoty' lub 'wpisz kwotę'
        self.kwota_txt = Text(self,  font = ('Calibri', 11),width = 110, height = 6, wrap = WORD, padx = 10, pady = 10)
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

#==================================================
#ZAMIANA CYFR NA SŁOWA
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


    def formattingTheEnteredNumber(self):
        '''Formatowanie wprowadzonej kwoty do obliczeń na format 0.00'''
        liczba_P = self.liczba_P.get()  #pobranie wprowadzonej kwoty
        liczba = liczba_P
        
        dl_liczba = len(liczba)   #długość liczba_P
        p = liczba.count('.')     #czy kropka dziesiętna jest w liczba_P

        d = None
        for i in range(dl_liczba):
            if liczba[i] == '.':
                d = i

        if p == 1:
            if d <= 12 and dl_liczba <= 15 and (dl_liczba - d) == 1:
                liczba = liczba + '00'
            if d <= 12 and dl_liczba <= 15 and (dl_liczba - d) == 2:
                liczba = liczba + '0'
            if d <= 12 and dl_liczba <= 15 and (dl_liczba - d) == 3:
                liczba = liczba
            if d <= 12 and (dl_liczba - d) >= 3:
                liczba = liczba[:d+1] + liczba[d+1:d+3]
            if d > 12:
                liczba = 'BŁĄD'
        else:
            if dl_liczba == 0:
                liczba = 'BŁĄD'
            elif 0 < dl_liczba <= 12:
                liczba = liczba + '.00'
            if dl_liczba > 12:
                liczba = 'BŁĄD'

        return liczba, liczba_P


    def amountInWords(self,liczba,format_gr):
        '''ZAMIANA CYFR NA SŁOWA'''
        #zamiana '.' na '0'
        przecinek = liczba[-3]
        liczba = liczba.replace(przecinek,'0')
        liczba_cc = liczba[:-3]    #część całkowita liczby

        #dopełnienie liczby krótszej niż 15 znaków znakami "0" - po lewej stronie
        liczba_c = ('0' * (15 - len(liczba))) + liczba   #liczba cała 15 znaków

        #[trojki] = [mld, mln, tys, setk, gr] #tablica 3-znakowych sekwencji liczb
        trojki = [] #tablica 3-znakowych sekwencji liczb
        trojki = [(liczba_c[j:j+3]) for (j) in range(0,15,3)]

        #tablica do zapisu słów z przekształcenia poszczególnych cyfr wpisanej liczby
        slowa = []
        
        #PĘTLA GŁÓWNA - cyfry na słowa
        #słowa dla cyfr - #słowo 'jeden','dziesięć','sto',

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

        #słowa dla trojek -'miliard/y/ów','milion/y/ów','tysiąc/e/ęcy','złoty/e/ych','grosz/e/y'

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

        #kwota słownie po usunięciu zbędnych znaków
        kwota_s = ''
        for m in range(20):
            kwota_s += slowa[m]
            if slowa[m]:
                kwota_s += ' '
            else:
                kwota_s += ''
            m += 1

        kwota_F = self.conversionToTheAccountingFormat(trojki)  #zamiana wpowadzonej liczby
                                                                #na format ###.###.###.##0,00
        return kwota_s, kwota_F
        #KONIEC zamiany 
    #==========================================

    def conversionToTheAccountingFormat(self,trojki):
        '''Zamiana wpowadzonej liczby na format księgowy ###.###.###.##0,00'''
      
        kwota_F = ''
        for s in range(5):
            kwota_F += trojki[s]+ '.'
      
        kwota_F = kwota_F[:19]

        if kwota_F[:17] == '000.000.000.000.0':
            kwota_F = '0.' + kwota_F[17:19]
        else:
            kwota_F1 = []
            kwota_F1 = [(kwota_F[i]) for i in range(19)]

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

    def amountInWordsOnTheScreen(self, kwota_s, liczba_P, kwota_F):
        '''Wpisanie kwoty słownie na ekranie'''
        first = '0'
        last = len(liczba_P)
        self.liczba_P.delete(first,last)

        napis_1 = 'Kwota podana:   '
        napis_2 = ' zł\t\t\t\t\t\t\t       Kwota w formacie księgowym:   '
        napis_3 = ' zł\nKwota słownie:   '
        napis_4 = '\n=====================\n'
        napis_5 = 'Kwota słownie została zapisana do pliku "kwota_slownie.txt"\n'
        napis = napis_1 + liczba_P + napis_2 + kwota_F + napis_3 + kwota_s + napis_4 + napis_5

        self.kwota_txt.delete(0.0, END)
        self.kwota_txt.insert(0.0, napis)
        self.format_gr.set(None)

    def enterTheAmountInWords(self,kwota_s, kwota_C):
        '''Wpisanie kwoty słownie do pliku 'kwota_slownie.txt'''

        self.checkingOfTheFile() #Sprawdzenie czy istnieje plik 'kwota_slownie.txt'
        with openFile("kwota_slownie.txt", "a") as plik:
            kwoty = ('\nKwota podana księgowo:\n',kwota_C,' zł','\nKwota słownie:\n',kwota_s,'\n')
            plik.writelines(kwoty)

    def checkingOfTheFile(self):
        '''Sprawdzenie czy istnieje plik kwota_slownie.txt,
           utworzenie go gdy nie istnieje a gdy istnieje sparwdzenie jego
           wielkosci - usunięcie początkowych linii gy jest ich ponad 50'''

        linie = []
        try:
            with openFile("kwota_slownie.txt", "r") as lin:  # odczytywanie linia po linii do listy
                linie = lin.readlines()
        except (UnicodeDecodeError, FileNotFoundError) :
            with openFile("kwota_slownie.txt", "w") as lin:
                lin.close()
        if len(linie) > 50:
            del linie[:10]
        with openFile("kwota_slownie.txt", "w") as lin:  # zapis linii
            lin.writelines(linie[:])

    def main(self):

        liczba, liczba_P = self.formattingTheEnteredNumber()   #Formatowanie wprowadzonej kwoty do obliczeń

        napis = liczba
        if napis == 'BŁĄD':
            napis = 'Niewłaściwy format wprowadzonej kwoty!\nWprowadż właściwą kwotę.'
            self.kwota_txt.delete(0.0, END)
            self.kwota_txt.insert(0.0, 'Kwota podana:' + liczba_P + '\n' + napis)
            first = '0'
            last = len(liczba_P)
            self.liczba_P.delete(first,last)
            self.format_gr.set(None)
        else:
            format_gr = self.format_gr.get()
            first = '0'
            last = len(self.liczba_P.get())
            self.liczba_P.delete(first,last)

            kwota_s, kwota_F = self.amountInWords(liczba,format_gr)
            self.amountInWordsOnTheScreen(kwota_s, liczba_P, kwota_F)#, napis_5)
            self.enterTheAmountInWords(kwota_s, kwota_F)    



#==============================================================================

# część główna
root = Tk()
root.title('Zamiana kwoty na tekst')
app = Apka(root)
root.mainloop()
