import sys
import os
from klasy import FileHandler
from magazyn import Magazyn


FOLDER = 'pliki'
PLIK_STARTOWY = FILE_INPUT = 'in.txt'
FILE_OUTPUT = 'history.txt'

# wczytanie z lini komend
file_path_input = sys.argv[1]
file_path_output = os.path.join(FOLDER, FILE_OUTPUT)

file_handler = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
file_handler.read_history()
# print(file_handler.history)
file_handler.write_history()

magazyn = Magazyn(file_handler.history)
magazyn.oblicz_aktualny_stan()
print(magazyn.stan_konta)
print(magazyn.stan_magazynowy)