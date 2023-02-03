from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lista = txt_importer(path_file)
    
    for i in instance.queue:
        if i['nome_do_arquivo'] == path_file:
            return None
    new_register = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lista),
        'linhas_do_arquivo': lista
        }
    instance.enqueue(new_register)
    # return print(new_register) # equivalente a linha abaixo
    return sys.stdout.write(str(new_register))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
