# -*- coding: utf-8 -*-
"""
Created on Fri May  7 19:32:25 2021

@author: Ada
"""

# Sprawdzanie obecnosci
# # Napisz program, ktory otwiera N (dwa lub wiecej) plikow tekstowych.
# W kazdej linii kazdego z tych plikow sa zapisane imie i nazwisko albo nazwisko i imie.
# Program ma przygotowac raport w ktorym podane beda imiona i nazwiska tych osob, 
# ktore nie zostaly odnotowane odpowiednio w N-1 plikach, N-2 plikach itd.

def zadanie2(*files):
	"""
	Zadanie 2: Sprawdzanie obecnosci
	"""
	print('Zadanie 2: Sprawdzanie obecnosci');

	# tworzymy pusty slownik
	# beda tam dopasowania 'student':liczba_obecnosci
	dziennik = {};

	# jezeli podano mniej niz 2 pliki, wyswietla napis i konczy
	if (len(files)<2):
		print('Incorrect number of input files');
		return;

	# dla kazdego z plikow / list obecnosci
	for file in files:
		print('Wczytywanie listy obecnosci z pliku: ' + file);
		# wczytuje zawartosc pliku wierszami
		with open(file) as f:
			content = f.read().splitlines();

		# dla kazdej linii w pliku
		for line in content:
			
			# wylicza nazwe studenta
			student = getCanonicalName(line);

			# pobieramy liczbe zajec, na ktorych byl student
			# 0 jest wartoscia, ktora zostanie zwrocona w przypadku, gdy studenta nie znalezlismy w dzienniku
			obecnosc = dziennik.get(student, 0);

			# zapisujemy studenta z obecnoscia zwiekszona o 1 do dziennika
			dziennik[student] = obecnosc+1;

	# posortowany dziennik
	sorted_dict = {}

	# w sorted_keys beda keye, czyli imie nazwisko studenta
	
	# sortujemy klucze dziennika
	# key=dziennik.get oznacza, ze porownywanc bedziemy wartosc przypisana dla danego klucza
	# w naszym przypadku: porownujemy liczbe obecnosci, a nie imie nazwisko studenta
	# reverse = True oznacza, ze chcemy sortowac malejaco
	sorted_keys = sorted(dziennik, key=dziennik.get, reverse = True)

	# dla kazdego imienia nazwiska w posortowanej liscie studentow
	for key in sorted_keys:
		# uzupelniamy posortowany dziennik 
		# key - nazwisko studenta
		# dziennik[key] zwraca liczbe obecnosci danego studenta
		# zapisujemy ta wawrtosc do posortowanego dziennika, dla tego samego studenta
	    sorted_dict[key] = dziennik[key]

	# wyswietlamy koncowa liste
	# dla kazdego studenta z dziennika
	for student in sorted_dict.keys():
		# wyswietlamy imie studenta oraz jego obecnosc
		# str(1) zamienia liczbe 1 na tekst '1'
		# bez tego nie mozna by uzyc znaku +
		# tzn: str + int jest niedozwolone (tekst + liczba)
		print(student + ' ' + str(dziennik[student]));


def getCanonicalName(name: str)->str:
	"""
	Zwraca nazwe studenta
	"""
	# wstawia ' ' miedzy imie i nazwisko studenta, posortowane alfabetycznie
	# dzieki temu 'Kowalski Adam' i 'Adam Kowalski' na roznych listach
	# beda wyszukiwani jako 'Adam Kowalski'
	# ale 'Adamiak Pawel' i 'Pawel Adamiak'
	# bedzie widnial jako 'Adamiak Pawel'
	# czyli raz bedzie imie nazwisko,
	# a raz nazwisko imie
	# kolejnosc alfabetyczna zadecyduje
	return ' '.join(sorted(name.split()));