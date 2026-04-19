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

    # тест получения жанра книги по её имени
    @pytest.mark.parametrize('book, genre',[['Тайна Коко','Мультфильмы']])
    def test_get_book_genre_name_book_success_get_genre(self, book, genre):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book(book)
        #добавляем жанр книге
        collector.set_book_genre(book, genre)
        #проверяем жанр у книги с жанром
        assert collector.get_book_genre(book) == genre

    #тест получения жанра несуществующей книги
    def test_get_book_genre_non_existent_book_genre_none(self):
        collector = BooksCollector()
        #проверяем жанр у книги с жанром
        assert collector.get_book_genre('Умка') == None

    # тестируем вывод списока книг с определённым жанром
    def test_get_books_with_specific_genre_genre_list_book_genre(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Дюна')
        collector.add_new_book('Основание')
        collector.add_new_book('Гиперион')
        collector.add_new_book('Приключения Тома Соера')
        #добавляем жанр книге
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Основание', 'Фантастика')
        collector.set_book_genre('Гиперион', 'Фантастика')
        collector.set_book_genre('Приключения Тома Соера', 'Мультфильмы')
        # проверяем список
        assert ['Дюна','Основание','Гиперион'] == collector.get_books_with_specific_genre('Фантастика')

    # тестируем вывод пустого списка книг с жанром не из списка, пустым жаром и ввод заглавными жанра
    @pytest.mark.parametrize('genre',['Ужас','','УЖАСЫ']) 
    def test_get_books_with_specific_non_existent_genre_genre_list_null(self, genre):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')
        collector.add_new_book('Дракула')
        #добавляем жанр книге
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        # проверяем список, что пуст
        assert collector.get_books_with_specific_genre(genre)==[]

    # тестируем вывод пустого списка книг с пустым списком книг
    def test_get_books_with_specific_non_book_genre_list_null(self):
        collector = BooksCollector()
        # проверяем список, что пуст
        assert collector.get_books_with_specific_genre('Комедии')==[] 

    # тест получения словаря books_genre
    def test_get_books_genre_add_book_list_book(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Киберпанк 2077')    
        #проверяем получения словаря
        assert collector.get_books_genre()=={'Киберпанк 2077':''}

    # тест получения пустого словаря books_genre
    def test_get_books_genre_null_list_book_list_book_null(self):
        collector = BooksCollector()
        #проверяем получения пустого словаря  
        assert collector.get_books_genre()=={}    

    # тест проверки возврата книг, подходящие детям
    def test_get_books_for_children_add_book_child_list_book_child(self):
        collector = BooksCollector()
        # добавляем книгу
        collector.add_new_book('Дюна')
        collector.add_new_book('Приключения Шурика')
        collector.add_new_book('Оно')
        collector.add_new_book('Приключения Тома Соера')
        #добавляем жанр книге
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Приключения Шурика', 'Комедии')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Приключения Тома Соера','Мультфильмы')
        #проверяем список
        assert collector.get_books_for_children()==['Дюна','Приключения Шурика','Приключения Тома Соера']
        