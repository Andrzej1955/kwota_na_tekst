# LICZBA NA TEKST
# Zamienia liczbę na tekst - słownie

import re

#przecinek = ""  #znak oddzielajacy część cakowita od części dziesiętnej
liczba = ""     #wczytana liczba
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
    #print('===================================================')
    #kwota słownie po usunieciu zbędnych znaków
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


def display(title):
    print(title)
    
def wybor():
    wynik_w = ''    #sterowanie wyborem: 'C' lub 'liczba'
    wynik = ''      #prawidłowa liczba przekazywana do przekształcenia
    liczba = ''     #wczytywana liczba
    pat = re.compile(r'[*]')    #zmienna 're' do sprawdzenia prawidłowosci wczytanej liczby
    while wynik_w != 'OK':
        print(
        '''
        ==========================================================
        Podaj kwotę w złotych z przedziału <0, 999.999.999.999,99>
        w formacie : ##.##0,00 lub ####0,00
        lub
        w formacie : ##,##0.00 lub ####0.00
        i składającą się tylko ze znaków: \'0123456789.,\'
        oraz wybierz format 'groszy'
        1/ - słowny          : 'zero groszy'
                                (format domyślny)
        2/ - liczbowo-słowny : '00 groszy'
        3/ - liczbowy        : '99/100'

        lub

        naciśnij klawisz \'C\' - \(Cancel\) aby zakończyc program.
        ==========================================================
        '''
        )
        liczba = input("\tKwota lub C': ").lower()
        if liczba != 'c':
            F_GR = '1,2,3'
            format_gr = input("\tFormat groszy '1,2,3': ")
            if format_gr not in F_GR:
                format_gr = '1'

        if liczba == 'c':
            wynik_w = 'OK'
            wynik = 'break'
            end(wynik)
        else:
            #sprawdzenie czy znaki liczby są prawidłowe - wyrażenie regex
            pat = re.compile(r'^[0-9]{0,3}[.,]?[0-9]{0,3}[.,]?[0-9]{0,3}[.,]?[0-9]{0,2}[0-9][.,][0-9]{2}$')
            #pat = re.compile(r'^[0-9]{0,11}[0-9][.,][0-9]{2}$')
            if not pat.match(liczba):
                wynik_w = '1'
            else:
                wynik = liczba
                wynik_w = wydruk(wynik,format_gr)

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
   

def end(wynik):
    if wynik == 'break':
        print(
        '''
        ===================================================
        Nacisnąłeś "C" - KONIEC DZIAŁANIA PROGRAMU
        DZIĘKUJEMY ZA SKORZYSTANIE Z PROGRAMU
        ===================================================
        '''
        )

def wydruk(wynik,format_gr):
    koniec = ''
    liczba = wynik
    kwota_s = zamiana(liczba,format_gr)
    kwota_C = liczba_F(kwota_)

    print('\t===================================================')
    print('\tKwota podana cyfrowo:')
    print('\t',kwota_C,'zł')
    print('\tKwota słownie:')
    print('\t',kwota_s)
    print('\t===================================================')
    plik = open("kwota_slownie.txt", "a")
    kwoty = ('\nKwota podana cyfrowo:\n',kwota_C,' zł','\nKwota słownie:\n',kwota_s,'\n')
    plik.writelines(kwoty)
    plik.close()
    print('\tKwota słownie została zapisana do pliku ')
    print('\t"kwota_slownie.txt"')
    print('\t===================================================\n\n\n')
    koniec = 'dalej'
    return koniec


#START

display(
        '''
        ===================================================
        \n\t\t\tLICZBY NA SŁOWA\n
        \t\t     WITAJ\n
        ===================================================
        '''
        )

wybor()
#print('liczba: ',liczba)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

