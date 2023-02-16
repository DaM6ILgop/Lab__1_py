numberToconvert = (float(input("Введите число для конвертации")))
rub = int(numberToconvert)# приведение строки к инту
assert numberToconvert >= 0 # проверка на то ,  что число больше нуля
kop = round((numberToconvert - rub)*100)
print(str(rub) + " руб. " + str(kop) + " коп.")


def format_money(amount):
    try:
        if amount < 0:
            raise ValueError("Negative amount")
        rubles = int(amount)
        kopecks = int(round((amount - rubles) * 100))
        return '{} руб. {} коп.'.format(rubles, kopecks)
    except ValueError as e:
        return 'Некорректный формат: {}'.format(e)

input_amount = float(input("Введите сумму: "))
print(format_money(input_amount))