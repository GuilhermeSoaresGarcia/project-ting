from ting_file_management.priority_queue import PriorityQueue
import pytest

case_one = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ['a', 'b', 'c']
    }

case_two = {
    "nome_do_arquivo": "arquivo_teste1.txt",
    "qtd_linhas": 5,
    "linhas_do_arquivo": ['a', 'b', 'c', 'd', 'e']
    }

case_three = {
    "nome_do_arquivo": "arquivo_teste2.txt",
    "qtd_linhas": 2,
    "linhas_do_arquivo": ['a', 'b']
    }


def test_basic_priority_queueing():
    test_priority_queue = PriorityQueue()
    test_priority_queue.enqueue(case_one)
    test_priority_queue.enqueue(case_two)
    test_priority_queue.enqueue(case_three)
    assert len(test_priority_queue.regular_priority) == 1
    assert len(test_priority_queue.high_priority) == 2
    assert test_priority_queue.regular_priority.queue[0] == case_two
    with pytest.raises(IndexError):
        test_priority_queue.search(10)
    assert test_priority_queue.high_priority.queue[1] == case_three
    test_priority_queue.dequeue()
    assert len(test_priority_queue) == 2
    assert test_priority_queue.search(0) == case_three
