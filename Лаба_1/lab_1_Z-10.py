import re

def check_password_strength(password):
    checks = []

    if len(password) < 8:
        checks.append("Пароль слишком короткий (меньше 8 символов)")
    if not re.search(r"\d", password):
        checks.append("Пароль должен содержать цифры")
    if not re.search(r"[A-Z]", password):
        checks.append("Пароль должен содержать заглавные буквы")
    if not re.search(r"[ !\"#$%&'()*+,-./[\\\]^_`{|}~""]", password):
        checks.append("Пароль должен содержать специальные символы")

    if not checks:
        print("Пароль надежный")
    else:
        print("Пароль недостаточно надежный:")
        for check in checks:
            print(check)
         

password = input("Введите пароль: ")
check_password_strength(password)