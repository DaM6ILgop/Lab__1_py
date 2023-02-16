print('Введите номер вашей карты')
result = ""
numberCard = input()
check = 0
for numCard in numberCard:
    if numCard.isdigit() and check >= 4 and check < len(numberCard) - 4:#Добавляем проверку на то, сколько цифр надо заменить.  Counter нужен как счетчик. если счетчик меньше 4-х, то мы не меняем ничего.Там же проверяям последние 4 цифры                                                                                                                                 
        result += '*'
    else:
        result += numCard
    check += 1 #Каждый проход цикла идет увеличение переменной. Как только она станет >= 4 и меньше длинны строки -4 символа, то цифры будут замененны на звездочки.
print(result)