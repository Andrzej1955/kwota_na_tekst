# liczba_tekst_okieno
# Tworzy okno do wpisania kwoty cyfrowo i uzyskania tekstu tej kwoty
# Wysietlanie i zapis do pliku tekstu kwoty

from tkinter import *
from src.libs import openFile

def checkingOfTheFile():
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

def enterTheAmountInWords(kwota_s, kwota_C):
    '''Wpisanie kwoty słownie do pliku 'kwota_slownie.txt'''

    checkingOfTheFile() #Sprawdzenie czy istnieje plik 'kwota_slownie.txt'
    with openFile("kwota_slownie.txt", "a") as plik:
        kwoty = ('\nKwota podana księgowo:\n',kwota_C,' zł','\nKwota słownie:\n',kwota_s,'\n')
        plik.writelines(kwoty)


