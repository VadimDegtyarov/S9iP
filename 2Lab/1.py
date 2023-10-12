def is_password_good(password):
    if len(password) >= 10:
        for el in password:
            Btitle = 0
            Blower = 0
            if el.istitle():
                Btitle = True
            if el.islower():
                Blower = True

        if Blower and Btitle == 0:
            print("Пароль должен содержать заглавную и строчную буквы")
            exit()
    else:
        print("пароль должен быть длиннее 10 символов")
        exit()
    print(f"Пароль {password} введен успешно")


is_password_good(input("Введите пароль"))
