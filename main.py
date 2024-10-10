
def password_symbol(password: str):
    digit = False
    for char in password:
        if char.isdigit():
            digit = True
    if digit:
        print("Есть цифра")
    else:
        print("Нет цифр")


if __name__ == "__main__":
    password = input("Введите пароль: ")

    if len(password) < 12:
        print("Короткий")
        password_symbol(password=password)
    else:
        password_symbol(password=password)
        print("Длинный")
