"""
Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.

Подготовка:
Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования.

Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
    1. Создавать локальный список all_data.
    2. Открывать файл name для чтения.
    3. Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
    4. Во время считывания добавлять каждую строку в список all_data.

Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.

    1. Создайте список названий файлов в соответствии с названиями файлов архива.
    2. Вызовите функцию read_info для каждого файла по очереди (линейно) и
    измерьте время выполнения и выведите его в консоль.
    3. Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
    контекстный менеджер with и объект Pool. Для вызова функции используйте метод map,
    передав в него функцию read_info и список названий файлов.
    Измерьте время выполнения и выведите его в консоль.

Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
предварительно закомментировав другой.

Примечания:
    1. Используйте конструкцию if __name__ == '__main__' при многопроссном подходе.
    2. Выводить или возвращать список all_data в функции не нужно. Можете сделать это,
    но кол-во информации в файлах достигает - 10^9 строк.
"""
import multiprocessing
import time


def read_info(name: str) -> None:
    """Считывает файл построчно и добавляет строки в список"""
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line.strip())
            if not line:
                break


# создаем список файлов (в нашем случае они находятся в той же папке, что и наш проект)
file_names = [f'./file {i}.txt' for i in range(1, 5)]

# линейно вызываем функцию read_info с каждым файлом из списка file_list
# замеряем и выводим время работы
start_time = time.time()
for file_name in file_names:
    read_info(file_name)
end_time = time.time()
res = end_time - start_time
print(f'Время выполнения {res:.2f} секунд(ы)')

# вызываем функцию read_info с каждым файлом из списка file_list используя многопроцессный подход
# поскольку мы заранее знаем, что в file_list у нас название 4-х файлов, то запустим 4 процесса
# замеряем время работы

# if __name__ == '__main__':
#     start_time = time.time()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     end_time = time.time()
#     res = end_time - start_time
#     print(f'Время выполнения {res:.2f} секунд(ы)')
