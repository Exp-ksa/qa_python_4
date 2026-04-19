# qa_python

# тестируем add_two_books - добавление двух книг
def test_add_new_book_add_two_books(self)

# тест добавления дубликата книги
def test_add_new_book_duplicate_not_added(self):

# тест добавления книги с длиной наименования нижние граничные значения 1, 2 и верхние граничные значения 39, 40
@pytest.mark.parametrize('book',['О','Мы','Убийство в восточном экспрессе номер 51','Звёздный рейд: Восстание киборгов Тартас'])
def test_add_new_book_name_limit_values_book_added(self, book):

# тест отсутвия книги с длиной наименования ноль символов и длиной 41 
@pytest.mark.parametrize('book',['','Тайна Лунного моря: Поиск артефакта богов'])
def test_add_new_book_name_lower_limit_book_not_added(self, book):

# тест отсутвия книги с длиной наименования ноль символов и длиной 41 
@pytest.mark.parametrize('book',['','Тайна Лунного моря: Поиск артефакта богов'])
def test_add_new_book_name_lower_limit_book_not_added(self, book):

# тестируем у добавленной книги нет жанра
def test_add_new_book_added_book_not_genre(self):

# тестируем устанавку жанра книге
def test_set_book_genre_sucsess(self):

# тест отсутсвия устанавки жанра несуществующей книге
def test_set_book_genre_non_existent_book_not_set_genre(self):

# тест получения жанра книги по её имени
@pytest.mark.parametrize('book, genre',[['Тайна Коко','Мультфильмы']])
def test_get_book_genre_name_book_success_get_genre(self, book, genre):

# тест получения жанра несуществующей книги
def test_get_book_genre_non_existent_book_genre_none(self):

# тестируем вывод списока книг с определённым жанром
def test_get_books_with_specific_genre_genre_list_book_genre(self):

# тестируем вывод пустого списка книг с жанром не из списка, пустым жаром и ввод заглавными жанра
@pytest.mark.parametrize('genre',['Ужас','','УЖАСЫ']) 
def test_get_books_with_specific_non_existent_genre_genre_list_null(self, genre):

# тестируем вывод пустого списка книг с пустым списком книг
def test_get_books_with_specific_non_book_genre_list_null(self):

# тест получения словаря books_genre
def test_get_books_genre_add_book_list_book(self):

# тест получения пустого словаря books_genre
def test_get_books_genre_null_list_book_list_book_null(self):

# тест проверки возврата книг, подходящие детям
def test_get_books_for_children_add_book_child_list_book_child(self):

# тест добавления книги в Избранное
def test_add_book_in_favorites_add_book_list_favorites(self):

# тест невозможность добавить книгу в избранное если список книг пуст
def test_add_book_in_favorites_no_book_list_favorites_null(self):

# тестируем удаляем книгу из Избранного
def test_delete_book_from_favorites_list_book_sucsess_delete_book(self):

# получаем список Избранных книг из двух книг
def test_get_list_of_favorites_books_add_two_favorites_get_list(self):
