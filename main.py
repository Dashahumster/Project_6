def degree(t):
    """Перевод из Фаренгейта в Цельсия"""
    t = (t-32)/1.8
    return t

def percent(pr):
    """Перевод в проценты"""
    pr = pr / 100
    return pr

def main():
    input_f = input('Введите название файла: ')
    _date = int(input('Введите день, в который хоите узнать наш прогноз: '))
    percent_in = int(input('Введите влпжность в %: '))
    try:
        with open(input_f, 'r') as f_in:
            with open('output.txt', 'w') as f_out:
                text = f_in.readlines()
                number = int(text[_date - 1])
                degree_n = int(degree(number))
                degree_n = round(degree_n)
                percent_in_1 = percent(percent_in)
                print('{} числа было {}'.format(_date, degree_n), file=f_out)
                if percent_in_1 > 0.51:
                    print('Скорее всего влажность высокая', file=f_out)
                else:
                    print('Скорее всего влажность низка', file=f_out)

    except FileNotFoundError:
        print('Файл "{}\" не найден.'.format(input_f))

if __name__=='__main__':
    main()