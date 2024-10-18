"""
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов
и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
1) get_all_words - подготовительный метод, который возвращает словарь следующего вида:
    {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    Где:
        1.'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
        2.['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

    Алгоритм получения словаря такого вида в методе get_all_words:
    1.Создайте пустой словарь all_words.
    2.Переберите названия файлов и открывайте каждый из них, используя оператор with.
    3.Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    4.Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
    (тире обособлено пробелами, это не дефис в слове).
    5.Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    6.В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

2) find(self, word) - метод, где word - искомое слово. Возвращает словарь,
    где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.

3) count(self, word) - метод, где word - искомое слово. Возвращает словарь,
    где ключ - название файла, значение - количество слова word в списке слов этого файла.

- В методах find и count пользуйтесь ранее написанным методом get_all_words
для получения названия файла и списка его слов.
- Для удобного перебора одновременно ключа(названия) и значения(списка слов)
можно воспользоваться методом словаря - item().
    for name, words in get_all_words().items():
      # Логика методов find или count

Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

Вывод на консоль:
{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для',
'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
{'test_file.txt': 3}
{'test_file.txt': 4}

Примечания:
    Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
    Решайте задачу последовательно - написав один метод, проверьте результаты его работы.
"""
from pprint import pprint


class WordsFinder:
    def __init__(self, *file_names):
        """
        Принимает неограниченное количество названий файлов
        и сохраняет их в атрибут file_names
        """
        self.file_names = file_names

    def get_all_words(self) -> dict:
        """
        Открывает каждый файл, считывает его содержимое и переводит в нижний регистр,
        удаляет пунктуацию и разбивает текст на слова.
        Возвращает словарь, где ключ - это название файла, а значение - список из слов.
        """
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punctuation, '')
                text = text.split()
                all_words[file.name] = text
        return all_words

    def find(self, word: str) -> dict:
        """
        Возвращает словарь в котором:
        Ключ - название файла.
        Значение - позиция указанного слова в файле (регист слова не учитывается).
        """
        word = word.lower()
        dict_ = {}
        for key, all_words in self.get_all_words().items():
            if word in all_words:
                dict_[key] = all_words.index(word) + 1
        return dict_

    def count(self, word: str) -> dict:
        """
        Возвращает словарь в котором:
        Ключ - название файла.
        Значение - количество указанного word в файле (регист word не учитывать).
        """
        word = word.lower()
        dict_ = {}
        for key, all_words in self.get_all_words().items():
            if word in all_words:
                dict_[key] = all_words.count(word)
        return dict_


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt', 'test_file_2.txt')
    pprint(finder2.get_all_words(), compact=1)  # Все слова
    print(finder2.find('TEXT'))  # {'test_file.txt': 3, 'test_file_2.txt': 7}
    print(finder2.count('teXT'))  # {'test_file.txt': 4, 'test_file_2.txt': 4}

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    pprint(finder1.get_all_words(), indent=1, width=170, compact=1)
    print(finder1.find('the'))
    print(finder1.count('the'))
