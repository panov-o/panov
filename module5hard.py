import time

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return
        else:
            print('Такой пользователь не найден')

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрировался и вошел в систему')

    def add(self, *args):
        for movie in args:
            for video in self.videos:
                if movie.title == video.title:
                    break
        else:
            self.videos.append(movie)

    def get_videos(self, text):
        list_movie = []
        print(text)
        for video in self.videos:
            if text.lower() in video.title.lower():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str):
        if self.current_user:
            for video in self.videos:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                if movie in video.title:
                    if video.time_now == 0:
                        video.time_now += 1
                    for i in range(video.time_now, video.duration + 1):
                        print(i, end = ' ')
                        time.sleep(1)
                    video.time_now = 0
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('язык'))
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



