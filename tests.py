import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #тест добавления дубликата книги
    def test_add_new_book_duplicate_not_added(self):
         # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Битва за битвой')
        collector.add_new_book('Битва за битвой')

        # проверяем, что добавилась только одна книга
        # словарь books_rating имеет длину 1
        assert len(collector.books_genre) == 1

    #тест добавления книги с длиной наименования нижние граничные значения 1, 2 и верхние граничные значения 39, 40
    @pytest.mark.parametrize('book',['О','Мы','Убийство в восточном экспрессе номер 51','Звёздный рейд: Восстание киборгов Тартас'])
    def test_add_new_book_name_limit_values_book_added(self, book):
         # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(book)
        
        # проверяем, что добавилась книга
        assert book in collector.books_genre.keys()

    #тест отсутвия книги с длиной наименования ноль символов и длиной 41 
    @pytest.mark.parametrize('book',['','Тайна Лунного моря: Поиск артефакта богов'])
    def test_add_new_book_name_lower_limit_book_not_added(self, book):
         # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book(book)
        
        # проверяем, что добавилась книга
        assert not book in collector.books_genre.keys()

    # тестируем у добавленной книги нет жанра
    def test_add_new_book_added_book_not_genre(self):
         # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Мстители')
    
        # проверяем, что у книги нет жанра
        assert collector.books_genre['Мстители'] == ''

    # тестируем устанавку жанра книге
    def test_set_book_genre_sucsess(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Франкенштейн')

        #добавляем жанр книге
        collector.set_book_genre('Франкенштейн', 'Ужасы')
        #проверяем установку жанра
        assert collector.books_genre['Франкенштейн'] == 'Ужасы'

    # тест отсутсвия устанавки жанра несуществующей книге
    def test_set_book_genre_non_existent_book_not_set_genre(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Другая книга')
        #добавляем жанр несуществующей книге
        collector.set_book_genre('Оно', 'Ужасы')
        #проверяем установку жанра
        assert 'Оно' not in collector.books_genre and collector.books_genre['Другая книга'] == ''