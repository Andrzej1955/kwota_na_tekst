# liczba_tekst_okieno
# Tworzy okno do wpisania kwoty cyfrowo i uzyskania tekstu tej kwoty
# Konwersja liczby na format księgowy


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
