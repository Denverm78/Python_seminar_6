# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

__all__ = ['check_date']

def _check_year(year): 
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True 
    else: 
        return False

def check_date(date_str):
    LONG_MONTH = [1, 3, 5, 7, 8, 10, 12]
    SHORT_MONTH = [4, 6, 9, 11]
    FEBRUARY = 2
    DAY_LONG_MONTH = 31
    DAY_SHORT_MONTH = 30
    DAY_LONG_FEBRUARY = 29
    DAY_SHORT_FEBRUARY = 28
    date_list = []
    for n in date_str.split("."):
        date_list.append(int(n))

    if 1 <= date_list[2] <= 9999:
        if date_list[1] in LONG_MONTH:
            if 1 <= date_list[0] <= DAY_LONG_MONTH:
                return True
            else: return False
        elif date_list[1] in SHORT_MONTH:
            if 1 <= date_list[0] <= DAY_SHORT_MONTH:
                return True
            else: return False    
        elif date_list[1] == FEBRUARY:
            if _check_year(date_list[2]) == True:
                if 1 <= date_list[0] <= DAY_LONG_FEBRUARY:
                    return True
                else: return False
            else: 
                if 1 <= date_list[0] <= DAY_SHORT_FEBRUARY:
                    return True
                else: return False
        else: return False
    else: return False


if __name__ == '__main__':
    # Чтобы проверить дату в терминале необходимо ввести в параметрах дату в формате DD.MM.YYYY
    file_name, *parametrs = argv
    date_from_param = str(parametrs[0])
    print(check_date(date_from_param))