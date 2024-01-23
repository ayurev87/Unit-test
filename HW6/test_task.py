import pytest

from task import NumbersList

@pytest.mark.parametrize('frist,second,result', [([],[1, 2, 3,4],(0, 3)),([1, 2, 3, 4], [] , (3, 0)), ([], [], [0, 0])])
def test_for_empty_list(frist, second, result):
    numbersList = NumbersList(frist, second)
    assert numbersList.get_list() == result

@pytest.mark.parametrize('frist,second,result', [([1], [1, 2, 3, 4, 5], (1, 3)), ([1, 2, 3, 4, 5], [1], (3, 1)), ([1], [1], (1, 1))])
def test_for_empty_list(frist, second, result):
    numbersList = NumbersList(frist, second)
    assert numbersList.get_list() == result

@pytest.fixture
def List1():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def List2():
    return [10,10]

def test_get_lists_averages(List1, List2):
    numbersList = NumbersList(List1, List2)
    assert numbersList.get_list() == (3, 10)

def test_checking_average_value_when_greater(List1, List2, capfd):
    numbersList = NumbersList(List2, List1)
    assert numbersList.list_comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Список1 среднее значение больше "

def test_checking_average_value_when_greater(List1, List2, capfd):
    numbersList = NumbersList(List1, List2)
    numbersList.list_comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Список 2 среднее значение больше"

def test_checking_average_value_when_greater(List1, List2, capfd):
    numbersList = NumbersList(List1, List1)
    numbersList.list_comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Списки равное среднее значение"

def test_init(List1, List2):
    numbersList = NumbersList(List1, List2)
    assert numbersList.frist == List1
    assert numbersList.second == List2