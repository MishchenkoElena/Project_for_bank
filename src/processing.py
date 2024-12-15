def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> list:
    '''
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию
'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению
    '''

    new_list_of_dictionaries = []