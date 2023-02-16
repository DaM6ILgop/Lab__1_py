print("Введите текст.")
print("Текст будет отсортирован по длинне слов")

input_text = input()
input_text_split = input_text.split() # разделение по пробелам

words_7Len = []
words_from_4_to_7 = []
another = []

for text in input_text_split:
    if len(text)>7:
        words_7Len.append(text)
    elif len(text) <= 4 and len(text) <= 7:
        words_from_4_to_7.append(text)
    else:
        another.append(text)
print(words_7Len)
print(words_from_4_to_7)
print(another)