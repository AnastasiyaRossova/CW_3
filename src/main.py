from src.utils import load_operations, sort_data, date_prettify, data_prettify
# # Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.

operations = load_operations('operations.json')
sort_operations = sort_data(operations)
sort_operations = sort_operations[:5]

for i in sort_operations:
    date = date_prettify(i['date'])
    description = i['description']
    from_ballans = i.get('from')
    to_ballans = data_prettify(i.get('to'))
    amount = i['operationAmount']['amount']
    name = i['operationAmount']['currency']['name']
    if from_ballans is None:
        print(f"{date} {description}")
        print(f"{to_ballans}")
        print(f"{amount} {name}")
    else:
        from_ballans = data_prettify(i.get('from'))
        print(f"{date} {description}")
        print(f"{from_ballans} -> {to_ballans}")
        print(f"{amount} {name}")
    print()







