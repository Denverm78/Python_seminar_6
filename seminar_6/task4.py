# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

from zagadka import zagad

print(zagad("Висит груша - нельзя скушать", ['лампа', 'лампочка', 'боксерская груша', 'груша повесилась'], 5))

