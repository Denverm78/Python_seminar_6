# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). 
# Функция формирует словарь с информацией о результатах отгадывания. 
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
# Для формирования результатов используйте генераторное выражение.

__all__ = ['dict_zagads', 'zagad', 'log_zagad', 'print_log', 'zagads_with_dict']

def zagad(secret, answers, number):
    print("Отгадайте загадку: ", secret)
    count = 0
    while count < number:
        user_answer = input("Ваш ответ: ").lower()
        count +=1
        if user_answer in answers:
            print("Угадали с ", count, " попытки")
            log_zag(secret, count)
            return(count)
        else:
            if count != number:
                print("Неверно, попробуйте еще раз")
            else:
                print("Неверно")
    print("С опытом узнаете... ")
    log_zag(secret, 0)
    return 0

def log_zag(text_zag, num_count):
    _log_answer[text_zag] = num_count

""" def print_log():
    for i in _log_answer:
        if _log_answer[i] == 0:
             print(f'Загадка: {i} - не отгадана')
        else:
             print(f'Загадка: {i} отгадана с {_log_answer[i]} попытки') """   

def print_log():
    print("Результаты угадывания: ")
    for key, value in _log_answer.items():
        print(key, value)     
        
def zagads_with_dict():
    myDict = {'2*2': '4', '3*3': '9', '4*4' : '16'}
    for i in myDict:
        zagad(i, myDict[i], 3)
    print_log()

_log_answer = {}
zagads_with_dict()