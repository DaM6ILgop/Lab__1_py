string = input("Enter a sentence: ")
out_char = []
for char in string:
    if string.count(char) == 1: #если в строке символ встречается 1 раз, то добавляем его в массив.
        out_char.append(char)
print("Буквы, которые входят в строку только 1 раз:", ''.join(out_char) ) #соединяем строки джоином и выводим