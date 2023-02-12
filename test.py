from ting_file_management.queue import Queue
from ting_file_management.file_process import process
from ting_word_searches.word_search import exists_word

fila = Queue()

process("./statics/arquivo_teste.txt", fila)

result = exists_word("acima", fila)

print(result)
