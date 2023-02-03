from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys

teste = Queue()
teste.enqueue({
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ['a', 'b', 'c']
})


def process(path_file, instance):
    txt_list = txt_importer(path_file)

    for i in instance.queue:
        if i['nome_do_arquivo'] == path_file:
            return None
    new_register = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_list),
        'linhas_do_arquivo': txt_list
        }
    instance.enqueue(new_register)
    # return print(new_register) # equivalente a linha abaixo
    return sys.stdout.write(str(new_register))


def remove(instance):
    try:
        file_name = instance.queue[0]['nome_do_arquivo']
        instance.queue.pop(0)
        return print(f'Arquivo {file_name} removido com sucesso')
    except IndexError:
        return print('Não há elementos')

# print(remove(teste))


def file_metadata(instance, position):
    try:
        file_name = instance.queue[position]
        return print(file_name)
    except IndexError:
        return sys.stderr.write('Posição inválida\n')

# print(file_metadata(teste, 1))
