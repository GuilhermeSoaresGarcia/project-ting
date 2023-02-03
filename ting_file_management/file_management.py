import sys
from pathlib import Path


def txt_importer(path_file):
    if Path(path_file).suffix != '.txt':
        return sys.stderr.write('Formato inválido')
    try:
        with open(path_file, 'r') as file:
            lista = file.readlines()
            return [line.strip() for line in lista]

    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')

# print(txt_importer("statics/arquivo_teste1.csv"))
