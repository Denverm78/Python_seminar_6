# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
 
__all__ = ['dict_zagads', 'zagad']

def zagad(secret, answers, number):
    print("Отгадайте загадку: ", secret)
    count = 0
    while count < number:
        user_answer = input("Ваш ответ: ").lower()
        count +=1
        if user_answer in answers:
            print("Угадали с ", count, " попытки")
            return(count)
        else:
            if count != number:
                print("Неверно, попробуйте еще раз")
            else:
                print("Неверно")
    print("С опытом узнаете... Пока-пока!")
    return 0
        
def dict_zagads():
    myDict = {'2*2': '4', '3*3': '9', '4*4' : '16'}
    for i in myDict:
        zagad(i, myDict[i], 3)

if __name__ == "__main__":

    dict_zagads()