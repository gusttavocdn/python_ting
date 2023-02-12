from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    result = []

    for i in range(len(instance.queue)):
        file = instance.queue[i]["nome_do_arquivo"]
        occurrences = [
            {
                "linha": i + 1,
            }
            for i, line in enumerate(instance.queue[i]["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file,
                    "ocorrencias": occurrences
                }
            )

    return result


def search_by_word(word: str, instance: Queue):
    result = []

    for i in range(len(instance.queue)):
        file = instance.queue[i]["nome_do_arquivo"]
        occurrences = [
            {
                "linha": i + 1,
                "conteudo": line
            }
            for i, line in enumerate(instance.queue[i]["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file,
                    "ocorrencias": occurrences
                }
            )

    return result
