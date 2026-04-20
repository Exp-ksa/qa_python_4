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

# тест установки жанра не из словаря genre
def test_set_book_genre_invalid_input_not_set(self):

# тест получения жанра книги по её имени
@pytest.mark.parametrize('book, genre',[['Тайна Коко','Мультфильмы']])
def test_get_book_genre_returns_correct_genre_when_set(self, book, genre):

# тест получения жанра несуществующей книги
def test_get_book_genre_returns_none_for_nonexistent_book(self):

# тестируем вывод списока книг с определённым жанром
def test_get_books_with_specific_genre_returns_correct_books(self):

# тестируем вывод пустого списка книг жанра не из списка, пустого жанра и жанра в верхнем регистре
@pytest.mark.parametrize('genre',['Ужас','','УЖАСЫ']) 
def test_get_books_with_specific_genre_returns_empty_for_invalid_genres(self, genre):

# тест: при пустой коллекции книг метод возвращает пустой список для любого жанра
def test_get_books_with_specific_genre_empty_collection_returns_empty(self):

# тест получения словаря books_genre
def test_get_books_genre_returns_dict_with_added_books(self):

# тест получения пустого словаря books_genre
def test_get_books_genre_returns_empty_dict_for_empty_collection(self):

# тест проверки возврата книг, подходящие детям
def test_get_books_for_children_returns_only_child_friendly_books(self):

# тест: книга успешно добавляется в избранное
def test_add_book_in_favorites_adds_book_to_favorites(self):

# тест: нельзя добавить книгу в избранное, если её нет в коллекции
def test_add_book_in_favorites_cannot_add_nonexistent_book(self):

# тестируем удаляем книгу из Избранного
def test_delete_book_from_favorites_successfully_removes_book(self):

# получаем список Избранных книг из двух книг
def test_get_list_of_favorites_books_returns_correct_selection(self):
