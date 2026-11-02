import pygame
import array
import random
import pickle
NAZWA_PLIKU = "dane.pkl"
tabela = None
try:
    with open(NAZWA_PLIKU, "rb") as plik:
        tabela = pickle.load(plik)
except FileNotFoundError:
    pass
if tabela is None:
    tabela = array.array("B")
pygame.init()
WYSOKOSC, SZEROKOSC = 600, 600
KOLOR_TLA = (128, 128, 128)
ROZMIAR_KRATKI = 200
ROZMIAR_LISTY = 9
DLUGOSC_LINIJKI = ROZMIAR_LISTY + 1
ZACZYNAJACY_GRACZ = random.randint(0, 1)
NAZWY_GRACZY = {0: "ty", 1: "AI"}
wygranaty = False
wygranaon = False
screen = pygame.display.set_mode((WYSOKOSC, SZEROKOSC))
pygame.display.set_caption("Kółko i krzyżyk AI")
clock = pygame.time.Clock()
kolko = pygame.image.load("kolko.svg")
krzyzyk = pygame.image.load("krzyzyk.svg")
indeks_list = {}
for i in range(len(tabela) // DLUGOSC_LINIJKI):
    start = i * DLUGOSC_LINIJKI
    lista_cyfr = tuple(tabela[start: start + ROZMIAR_LISTY])
    if lista_cyfr not in indeks_list:
        indeks_list[lista_cyfr] = []
    indeks_list[lista_cyfr].append(i)
akcja = None
gracz_teraz = ZACZYNAJACY_GRACZ
plansza = [0, 0, 0,
           0, 0, 0,
           0, 0, 0]
def narysuj_siatke():
    for x in range(0, SZEROKOSC, ROZMIAR_KRATKI):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, WYSOKOSC), 2)
    for y in range(0, WYSOKOSC, ROZMIAR_KRATKI):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (SZEROKOSC, y), 2)
def narysuj_obiekty():
    for indeks, wartosc in enumerate(plansza):
        if indeks == 0:
            pozycja = [0, 0]
        elif indeks == 1:
            pozycja = [200, 0]
        elif indeks == 2:
            pozycja = [400, 0]
        elif indeks == 3:
            pozycja = [0, 200]
        elif indeks == 4:
            pozycja = [200, 200]
        elif indeks == 5:
            pozycja = [400, 200]
        elif indeks == 6:
            pozycja = [0, 400]
        elif indeks == 7:
            pozycja = [200, 400]
        else:
            pozycja = [400, 400]
        if wartosc == 1:
            screen.blit(kolko, (pozycja[0], pozycja[1]))
        elif wartosc == 2:
            screen.blit(krzyzyk, (pozycja[0], pozycja[1]))
def zamien_obiekt(ktory, kto):
    global gracz_teraz
    if plansza[ktory] == 0:
        if kto == 0:
            dodaj_linijke(plansza, ktory)
            plansza[ktory] = 1
            gracz_teraz = 1
        else:
            plansza[ktory] = 2
            gracz_teraz = 0
def sprawdz_wygranaty():
    global wygranaty, uruchomiony
    if (plansza[0] == 1 and plansza[1] == 1 and plansza[2] == 1) or (plansza[3] == 1 and plansza[4] == 1 and plansza[5] == 1) or (plansza[6] == 1 and plansza[7] == 1 and plansza[8] == 1) or (plansza[0] == 1 and plansza[3] == 1 and plansza[6] == 1) or (plansza[1] == 1 and plansza[4] == 1 and plansza[7] == 1) or (plansza[2] == 1 and plansza[5] == 1 and plansza[8] == 1) or (plansza[0] == 1 and plansza[4] == 1 and plansza[8] == 1) or (plansza[2] == 1 and plansza[4] == 1 and plansza[6] == 1):
        wygranaty = True
        uruchomiony = False
def sprawdz_wygranaon():
    global wygranaon, uruchomiony
    if (plansza[0] == 2 and plansza[1] == 2 and plansza[2] == 2) or (plansza[3] == 2 and plansza[4] == 2 and plansza[5] == 2) or (plansza[6] == 2 and plansza[7] == 2 and plansza[8] == 2) or (plansza[0] == 2 and plansza[3] == 2 and plansza[6] == 2) or (plansza[1] == 2 and plansza[4] == 2 and plansza[7] == 2) or (plansza[2] == 2 and plansza[5] == 2 and plansza[8] == 2) or (plansza[0] == 2 and plansza[4] == 2 and plansza[8] == 2) or (plansza[2] == 2 and plansza[4] == 2 and plansza[6] == 2):
        wygranaon = True
        uruchomiony = False
def sprawdz_remis():
    global uruchomiony
    if 0 not in plansza:
        uruchomiony = False
def dodaj_linijke(lista_cyfr, pojedyncza_wartosc):
    nowy_indeks_wiersza = len(tabela) // DLUGOSC_LINIJKI
    tabela.fromlist(lista_cyfr)
    tabela.append(pojedyncza_wartosc)
    klucz_szukania = tuple(lista_cyfr)
    if klucz_szukania not in indeks_list:
        indeks_list[klucz_szukania] = []
    indeks_list[klucz_szukania].append(nowy_indeks_wiersza)
def szukaj_calych_wierszy(szukana_plansza):
    klucz = tuple(szukana_shapes := szukana_plansza)
    if klucz not in indeks_list:
        return []
    wyniki = []
    for indeks_wiersza in indeks_list[klucz]:
        start = indeks_wiersza * DLUGOSC_LINIJKI
        koniec = start + DLUGOSC_LINIJKI
        pelny_wiersz = list(tabela[start:koniec])
        wyniki.append(pelny_wiersz)
    return wyniki
uruchomiony = True
while uruchomiony:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiony = False
        if gracz_teraz == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mysz, y_mysz = event.pos
                if event.button == 1:
                    pole = (x_mysz // 200) + (y_mysz // 200) * 3
                    if pole in range(9):
                        zamien_obiekt(pole, 0)
                        sprawdz_wygranaty()
                        sprawdz_wygranaon()
                        sprawdz_remis()
    if uruchomiony and gracz_teraz == 1:
        plansza_z_perspektywy_czlowieka = []
        for pole in plansza:
            if pole == 1:  # Twoje kółko staje się znakiem przeciwnika
                plansza_z_perspektywy_czlowieka.append(2)
            elif pole == 2:  # Krzyżyk AI staje się znakiem gracza ("1")
                plansza_z_perspektywy_czlowieka.append(1)
            else:
                plansza_z_perspektywy_czlowieka.append(0)
        wyniki = szukaj_calych_wierszy(plansza_z_perspektywy_czlowieka)
        if wyniki:
            wybrany_wiersz = random.choice(wyniki)
            decyzja = wybrany_wiersz[9]
            if plansza[decyzja] == 0:
                zamien_obiekt(decyzja, 1)
            else:
                # Awaryjnie ruch losowy, gdyby pole z historii było zajęte
                losowe_pola = [i for i, v in enumerate(plansza) if v == 0]
                if losowe_pola:
                    zamien_obiekt(random.choice(losowe_pola), 1)
        else:
            losowe_pola = [i for i, v in enumerate(plansza) if v == 0]
            if losowe_pola:
                zamien_obiekt(random.choice(losowe_pola), 1)
        sprawdz_wygranaty()
        sprawdz_wygranaon()
        sprawdz_remis()
    screen.fill(KOLOR_TLA)
    narysuj_obiekty()
    narysuj_siatke()
    pygame.display.flip()
    clock.tick(30)
with open(NAZWA_PLIKU, "wb") as plik:
    pickle.dump(tabela, plik)
pygame.quit()