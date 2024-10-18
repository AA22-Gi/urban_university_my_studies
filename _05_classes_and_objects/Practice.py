class Databace:
    def __init__(self):
        self.date = {}

    def add_user(self, username, password):
        self.date[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    databace = Databace()
    while True:
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in databace.date:
                if password == databace.date[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль.')
            else:
                print('Пользователь не найден.')
        if choice == 2:
            user = User(input('Введите Ваше имя: '),
                        password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if password != password2:
                print('Пароли не совпадают, попробуйте ещё раз.')
                continue
            databace.add_user(user.username, user.password)
