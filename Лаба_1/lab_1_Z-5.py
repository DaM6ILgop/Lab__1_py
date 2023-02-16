input_string = input('Введите строку')
string  = input_string.split() #разделяет строку по пробелам на список слов 

new_mas_string = []

for str in string: 
    if str[0].isupper(): #проверяем строку с нулевого идекса на заглавную букву. если буква заглавная , то мы добавляем строку в массив с приведением в верхний регистр
        new_mas_string.append(str.upper())
    else:
        new_mas_string.append(str)
print("=" * 20)
print(" ".join(new_mas_string)) #Join создает новую строку, соединяя все элементы списка. пустые ковычки работают как сплит, разделяют строки по пробелам



