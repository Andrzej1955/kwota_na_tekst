# liczba_tekst_okieno
# Tworzy okno do wpisania kwoty cyfrowo i uzyskania tekstu tej kwoty
# Wysietlanie i zapis do pliku tekstu kwoty

from tkinter import *
from src.libs import openFile

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

def enterTheAmountInWords(self,kwota_s, kwota_C):
    '''Wpisanie kwoty słownie do pliku 'kwota_slownie.txt'''

    checkingOfTheFile(self) #Sprawdzenie czy istnieje plik 'kwota_slownie.txt'
    with openFile("kwota_slownie.txt", "a") as plik:
        kwoty = ('\nKwota podana księgowo:\n',kwota_C,' zł','\nKwota słownie:\n',kwota_s,'\n')
        plik.writelines(kwoty)


