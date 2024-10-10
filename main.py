
def password_symbol(password: str):
    digit = False
    for sign in password:
        if sign.isdigit():
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
    for sign in password:
        if sign.isdigit():
            digit = True
    if digit:
        return digit
    else:
        return digit


def password_rating(password: str):
    scope = 0

    how_long_pass = is_very_long(password=password)
    has_digit_in_pass = has_digit(password=password)
    if has_digit_in_pass:
        scope += 2
    if how_long_pass:
        scope += 2
    return scope


if __name__ == "__main__":
    password = input("Введите пароль: ")
    # print(is_very_long(password=password))
    # print(has_digit(password=password))
    print(password_rating(password=password))
