"""
Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы,
где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.).
Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов,
которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
авторизации и регистрации пользователя и т.д.

Подробное ТЗ:
Каждый объект класса User должен обладать следующими атрибутами и методами:
    - Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)

Каждый объект класса Video должен обладать следующими атрибутами и методами:
    - Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))

Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
    - Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    - Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users
    с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
    Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    - Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
    если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
    "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
    - Метод log_out для сброса текущего пользователя на None.
    - Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
    если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
    - Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих
    поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
    - Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
    то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    После текущее время просмотра данного видео сбрасывается.

Для метода watch_video так же учитывайте следующие особенности:
    1. Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
    2. Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
    В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
    3. Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
    Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
    4. После воспроизведения нужно выводить: "Конец видео"

Примечания:
Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др.
Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает,
тестировать разные вариации.
"""
from time import sleep


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname and hash(password) == hash(user.password):
                self.current_user = user
                return

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video_object in args:
            if video_object.title not in [v.title for v in self.videos]:
                self.videos.append(video_object)

    def get_videos(self, word: str):
        videos_title = []
        for video_object in self.videos:
            if word.lower() in video_object.title.lower():
                videos_title.append(video_object.title)
        return videos_title

    def watch_video(self, name_video: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == name_video:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for i in range(video.duration):
                    print(i + 1, end=' ')
                    video.time_now += 1
                    sleep(1)
                print("конец видео")
                video.time_now = 0
                return


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
