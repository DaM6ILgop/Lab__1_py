def сheck(list):
    for i in range(len(list) - 1):
        if list[i]>list[i+1]: #проверка на то, что след. число больше на единицу, т.е значения возрастают последовательно
            return False
    return True # возвращаем фолс если значения возрастают неравномерно, т.е, след значение больше на 2 

list = [1, 4, 3 ,5 ,7]
print(сheck(list))

list2 = [1,2,3,4,5,6]
print(сheck(list2))