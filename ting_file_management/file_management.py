import sys


def txt_importer(path_file: str):
    if not path_file.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, 'r') as file:
            content_list = list()
            for line in file:
                content_list.append(line.strip())
        return content_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
