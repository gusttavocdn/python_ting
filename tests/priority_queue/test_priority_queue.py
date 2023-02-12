from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    sut = PriorityQueue()
    value1 = {"qtd_linhas": 4}
    value2 = {"qtd_linhas": 6}
    value3 = {"qtd_linhas": 2}

    assert sut.is_priority(value1)
    assert not sut.is_priority(value2)

    sut.enqueue(value1)
    sut.enqueue(value2)
    sut.enqueue(value3)

    assert len(sut) == 3

    rm_value = sut.dequeue()
    assert rm_value == value1
    assert len(sut.high_priority) == 1

    rm_value = sut.dequeue()
    assert rm_value == value3
    assert len(sut.high_priority) == 0

    sut.enqueue(value1)
    sut.enqueue(value3)

    assert sut.search(1) == value3
    assert sut.search(0) == value1

    with pytest.raises(IndexError):
        sut.search(9999)
