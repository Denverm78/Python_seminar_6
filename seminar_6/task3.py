# Улучшаем задачу 2. 
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. 
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. 
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

__all__ = ['gen']

from sys import argv
from random import randint

def gen(min_number, max_number, count):
    random_number = randint(min_number, max_number + 1)
    print("Загадано", random_number)
    print(f"Угадайте число от {min_number} до {max_number} за {count} попыток")
    while count > 0:
        user_number = int(input("Введите свое число: "))
        if user_number < random_number:
            print("Больше")
            count -=1
        elif user_number > random_number:
            print("Меньше")
            count -=1
        else:
            print("Угадали!")
            return True
    return False

if __name__ == "__main__":
    file_name, *parametrs = argv
    gen(*(int(n) for n in parametrs))
    