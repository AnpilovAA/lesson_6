
def password_symbol(password: str):
    for char in password:
        if char.isdigit():
            print(char, "-", "Цифра")
        else:
            print(char, "-", "Буква")


if __name__ == "__main__":
    password = input("Введите пароль: ")

    if len(password) < 12:
        print("Короткий")
        password_symbol(password=password)
    else:
        password_symbol(password=password)
        print("Длинный")
