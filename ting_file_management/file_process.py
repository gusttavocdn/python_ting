from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file: str, instance: Queue):
    for i in range(len(instance.queue)):
        if (instance.queue[i]["nome_do_arquivo"] == path_file):
            return

    content = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }

    instance.enqueue(file_dict)

    print(file_dict)


def remove(instance: Queue):
    if instance.is_empty():
        return print("Não há elementos")

    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position: int):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
