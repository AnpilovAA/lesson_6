

if __name__=="__main__":
    password = input("Введите пароль: ")
    if len(password) < 12:
        print("Короткий")
    else:
        print("Длинный")
