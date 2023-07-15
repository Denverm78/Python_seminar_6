# Вспомните какие модули вы уже проходили на курсе. 
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

import sys
from random import randint as rnd
from math import tanh as tangenc, sqrt as sq
from time import timezone as tz
from sys import argv


print(rnd(1,11))
print(tangenc(90))
print(sys)
print(tz)
print(int(sq(121)))
print(argv)