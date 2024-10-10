
def password_symbol(password: str):
    digit = False
    for char in password:
        if char.isdigit():
            digit = True
    if digit:
        print("Есть цифра")
    else:
        print("Нет цифр")


def is_very_long(password: str) -> bool:
    if len(password) < 12:
        return False
    else:
        return True


def has_digit(password: str) -> bool:
    digit = False
    for char in password:
        if char.isdigit():
            digit = True
    if digit:
        return digit
    else:
        return digit


if __name__ == "__main__":
    password = input("Введите пароль: ")
    print(is_very_long(password=password))
    print(has_digit(password=password))
