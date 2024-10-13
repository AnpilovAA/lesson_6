from urwid import Edit, Text, Pile, Filler, MainLoop, connect_signal


def is_very_long(password: str) -> bool:
    return len(password) >= 12


def has_digit(password: str) -> bool:
    return any(sign.isdigit() for sign in password)


def has_letters(password: str) -> bool:
    return any(sign.isalpha() for sign in password)


def has_upper_letters(password: str) -> bool:
    return any(sing.isupper() for sing in password)


def has_lower_letters(password: str) -> bool:
    return any(sing.islower() for sing in password)


def has_symbols(password: str) -> bool:
    return any(not sign.isdigit() and not sign.isalpha() for sign in password)


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


def on_ask_change(edit, password):
    reply.set_text(password_rating(password=password))


if __name__ == "__main__":
    ask = Edit("Введите пароль: ", mask="*")
    reply = Text("")
    menu = Pile([ask, reply])
    menu = Filler(menu, valign="top")
    connect_signal(ask, "change", on_ask_change)
    MainLoop(menu).run()

    on_ask_change(ask, password_rating)
    password = "12dasc!gfW9112"
    print(password_rating(password=password))
