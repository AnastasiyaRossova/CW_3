from src.utils import date_prettify, data_prettify, load_operations, sort_data


def test_date_prettify():
    """Проверяет преобразование даты в формат ДД.ММ.ГГГГ"""
    assert date_prettify("2023-08-13T12:34:56") == "13.08.2023"
    assert date_prettify("2022-05-01T18:45:30") == "01.05.2022"
    assert date_prettify("2018-03-09T02:11:01.339352") == "09.03.2018"


def test_data_prettify():
    """Проверяет преобразование счета в формат **ХХХХ и номера карты в формат ХХХХ ХХ** **** ХХХХ"""
    assert data_prettify("Счет 75106830613657916952") == "Счет **6952"
    assert data_prettify("Visa Platinum 7000123456786361") == "Visa Platinum 7000 12** **** 6361"
    assert data_prettify("MasterCard 5555123456787890") == "MasterCard 5555 12** **** 7890"


t_2 = [
    {
        "state": "EXECUTED",
        "date": "2018-01-21T01:10:28.317704"
    },
    {
        "state": "EXECUTED",
        "date": "2019-09-29T14:25:28.588059"
    }
]


def test_sort_data():
    """Проверяет сортировку списка по статусу и дате"""
    assert sort_data(t_2) == [{'state': 'EXECUTED', 'date': '2019-09-29T14:25:28.588059'},
                              {'state': 'EXECUTED', 'date': '2018-01-21T01:10:28.317704'}]
