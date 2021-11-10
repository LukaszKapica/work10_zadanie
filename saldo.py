import sys
import os
from klasy import FileHandler
from magazyn import Magazyn


FOLDER = 'pliki'
FILE_INPUT = 'history.txt' # wczytywany z linii komend
FILE_OUTPUT = 'history.txt'

# wczytanie z lini komend
file_path_input = sys.argv[1]
file_path_output = os.path.join(FOLDER, FILE_OUTPUT)

file_handler = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
file_handler.read_history()
# print(file_handler.history)
file_handler.write_history()

magazyn = Magazyn(file_handler.history)
komenda = ['saldo', int(sys.argv[2]), sys.argv[3]]
file_handler.history.append(komenda)
magazyn.oblicz_aktualny_stan()
# print(file_handler.history)
print(magazyn.stan_konta)
file_handler.write_history()