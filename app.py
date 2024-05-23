# TODO опишите здесь функции для решения задачи


#if __name__ == '__main__':
    # TODO запустите здесь все необходимые функции

def enternumber(enter_str):
    norm = True
    while norm:
        try:
            num = float(input(enter_str))
            norm = False
        except:
            print('Введите число заново')
    return num


def operation1():
    while True:
        oper = input('Выберите операцию: ')
        if oper == '+':
            return first + second
        elif oper =='-':
            return first - second
        elif oper == '*':
            return first * second
        elif oper == '/':
            return first / second
        else:
            print('Некорректная операция')

print('Привет!')
first = enternumber('Введите первое число: ') #float(input('Введите число: '))
second = enternumber('Введите второе число: ') #float(input('Введите число: '))
print('Результат: ', operation1())