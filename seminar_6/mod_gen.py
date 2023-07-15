# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

__all__ = ['gen']

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
    print (gen(10,20,5))