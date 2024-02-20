import json


def load_operations(file_path):
    """
    Загружает список операций клиента
    """
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)


def sort_data(operations):
    """
    Принимает неотсортированный список операций клиента
    Выводит список успешеных операций, сортированных по дате
    """
    dict_operation = []
    for element in operations:
        for k, v in element.items():
            if element not in dict_operation and element["state"] == "EXECUTED":
                dict_operation.append(element)

    dict_operation = sorted(dict_operation, key=lambda data: data['date'], reverse=True)
    return dict_operation


def date_prettify(date: str) -> str:
    """
    Получает дату из списка
    Выводит преобразованную дату в виде ДД.ММ.ГГГГ
    """
    date_new = date[0:10].split('-')
    date_new = ".".join(ch for ch in reversed(date_new))
    return date_new


def data_prettify(from_data: str) -> str:
    """
    Получает информацию откуда и куда совершен перевод
    Выводит преобразованную информацию в формате:
    номер карты XXXX XX** **** XXXX; номер счета XXXX
    "Maestro 1596837868705199"
    """
    from_data_split = from_data.split(' ')
    num = from_data_split[-1]
    if from_data_split[0] == 'Счет':
        return f'{from_data_split[0]} **{num[-4:]}'

    if from_data_split[0] == 'Visa' and len(from_data_split) == 3:
        return f'{from_data_split[0]} {from_data_split[1]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'

    return f'{from_data_split[0]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'






