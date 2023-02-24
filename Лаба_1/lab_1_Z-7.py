stroka_1 = "www.pinterest.com"
stroka_2 = "fonts.google"

#добавляет в строку префикс, если начало строка начинается с www, иначе конкатенирует все сразу + .com
result_string_1= ["http://" + stroka_1 if stroka_1.startswith("www") else "http://www." + stroka_1 + ".com" ]
result_string_2 = ["http://" + stroka_2 if stroka_2.startswith("www") else "http://www." + stroka_2 + ".com"]

print(result_string_1)
print(result_string_2)

