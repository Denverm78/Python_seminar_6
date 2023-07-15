# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

__all__ = ['print_board', 'check_board', 'convert_figures', 'random_boards']

from random import randint, shuffle

def random_boards():
    # Чтобы ускорить поиск, расставляем ферзей по одному в каждом горизонтальном ряду
    # в случайном порядке, а в вертикальных рядах - в случайном порядке.
    line = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle(line)
    rf1 = [line[0], randint(1, 8)]
    rf2 = [line[1], randint(1, 8)]
    rf3 = [line[2], randint(1, 8)]
    rf4 = [line[3], randint(1, 8)]
    rf5 = [line[4], randint(1, 8)]
    rf6 = [line[5], randint(1, 8)]
    rf7 = [line[6], randint(1, 8)]
    rf8 = [line[7], randint(1, 8)]
    return rf1, rf2, rf3, rf4, rf5, rf6, rf7, rf8
    

def convert_figures(f1, f2, f3, f4, f5, f6, f7, f8):
        all_f = [f1, f2, f3, f4, f5, f6, f7, f8]
        gorizonts = []
        verticals = []
        for i in all_f:
            gorizonts.append(i[0])
            verticals.append(i[1])
        # print_board(all_f)
        return gorizonts, verticals

def print_board(all_f):
    board = []
    for i in range(8):
        line = []
        for j in range(8):
            if [i+1, j+1] in all_f:
                line.append('■')
            else:
                line.append('o')
        board.append(line)           
    for i in board:
        print(*i)
        
def check_board(x, y):
    for i in range(8):
        for j in range(i+1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False, x, y
    return True, x, y 

def start():
    count = 4 # Количество успешных расстановок
    print("Успешные варианты: ")
    while count > 0: 
        f1, f2, f3, f4, f5, f6, f7, f8 = random_boards()
        gorizont, vertical = convert_figures(f1, f2, f3, f4, f5, f6, f7, f8)
        ctrl, gorizont, vertical = check_board(gorizont, vertical)
        if ctrl == True:
            all_rf = []
            for i in range(8):
                all_rf.append([gorizont[i], vertical[i]])
            print(all_rf)    
            print_board(all_rf)
            count -= 1      


if __name__ == "__main__":
    
    start()
    
    
        