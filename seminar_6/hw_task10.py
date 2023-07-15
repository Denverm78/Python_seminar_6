# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

__all__ = ['print_board', 'check_board', 'convert_figures']

def convert_figures(f1, f2, f3, f4, f5, f6, f7, f8):
        all_f = [f1, f2, f3, f4, f5, f6, f7, f8]
        gorizonts = []
        verticals = []
        for i in all_f:
            gorizonts.append(i[0])
            verticals.append(i[1])
        print_board(all_f)
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
                return False
    return True        


if __name__ == "__main__":
    
    # Ферзи бьют друг друга:
    # f1 = [1, 2]
    # f2 = [2, 5]
    # f3 = [3, 8]
    # f4 = [4, 4]
    # f5 = [5, 2]
    # f6 = [6, 6]
    # f7 = [7, 4]
    # f8 = [8, 1]
    
    # Ферзи не бьют друг друга
    f1 = [1, 3]
    f2 = [2, 6]
    f3 = [3, 4]
    f4 = [4, 1]
    f5 = [5, 8]
    f6 = [6, 5]
    f7 = [7, 7]
    f8 = [8, 2]

    gorizont, vertical = convert_figures(f1, f2, f3, f4, f5, f6, f7, f8)
    print(check_board(gorizont, vertical))
