from ting_file_management.queue import Queue

teste = Queue()
teste.enqueue({
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ['Come abacAte', 'pra fazer', 'cocô bonito abacate']
})


def exists_word(word, instance):
    result = []
    word_occurrecies = []
    for queue_entry in instance.queue:
        # FONTE: https://stackoverflow.com/a/28072982/18172843
        for index, line in enumerate(queue_entry['linhas_do_arquivo']):
            if word.upper() in line.upper():
                word_occurrecies.append({'linha': index + 1})
    if len(word_occurrecies) > 0:
        result.append(
            {
                "palavra": word,
                # FONTE: https://stackoverflow.com/a/13207713/18172843
                "arquivo": ", ".join(
                    [file['nome_do_arquivo'] for file in instance.queue]
                    ),
                "ocorrencias": word_occurrecies
            }
        )
        return result
    return word_occurrecies


# print(exists_word('abacate', teste))


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
