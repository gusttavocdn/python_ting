from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return self.queue.__len__()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        value = self.queue.pop(0)
        return value

    def search(self, index: int):
        if 0 <= index < len(self.queue):
            return self.queue[index]
        raise IndexError("Index out of range")

    def is_empty(self):
        return not bool(len(self.queue))

    def __str__(self):
        str_items = ""
        for i in range(len(self.queue)):
            value = self.queue[i]
            str_items += str(value)
            if i + 1 < len(self.queue):
                str_items += ", "
        return "Queue(" + str_items + ")"
