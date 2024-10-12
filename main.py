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
            break
    if digit:
        return digit
    else:
        return digit


def has_letters(password: str) -> bool:
    letter = False
    for sign in password:
        if sign.isalpha():
            letter = True
            break
    if letter:
        return letter
    else:
        return letter


def has_upper_letters(password: str) -> bool:
    upper_letter = False
    for sing in password:
        if sing.isupper():
            upper_letter = True
            break
    if upper_letter:
        return upper_letter
    else:
        return upper_letter


def has_lower_letters(password: str) -> bool:
    lower_letter = False
    for sing in password:
        if sing.islower():
            lower_letter = True
            break
    if lower_letter:
        return lower_letter
    else:
        return lower_letter

def has_symbols(password: str) -> bool:
    symbol = False
    for sign in password:
        if not sign.isdigit() and not sign.isalpha():
            symbol = True
            break
    if symbol:
        return symbol
    else:
        return symbol


def password_rating(password: str) -> str:
    scope = 0

    check_conditions = [
        is_very_long(password=password),
        has_digit(password=password),
        has_letters(password=password),
        has_upper_letters(password=password),
        has_lower_letters(password=password),
        has_symbols(password=password)
    ]

    for check_result in check_conditions:
        if check_result:
            scope += 2
    
    return f"Рейтинг пароля: {scope}"


if __name__ == "__main__":
    # password = input("Введите пароль: ")
    password = "12dasc!gfW9112"
    print(password_rating(password=password))
