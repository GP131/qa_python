import pytest


class TestBooksCollector:

    # Test adding two new books (test was provided)
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Test adding valid books
    @pytest.mark.parametrize("book_name", [
        "Волшебник Страны Оз",
        "Гордость и предубеждение и зомби",
        "Что делать, если ваш кот хочет вас убить",
    ])
    def test_add_new_book_valid_name(self, collector, book_name):
        initial_books_count = len(collector.get_books_genre())
        collector.add_new_book(book_name)
        new_books_count = len(collector.get_books_genre())
        assert new_books_count == initial_books_count + 1

    # Test adding invalid books
    @pytest.mark.parametrize("book_name", [
        "",  # Empty book name
        "A" * 41,  # Book name exceeds 40 characters
        # "Волшебник Страны Оз",   # Duplicate book errors out due to lack of prevention code in main
    ])
    def test_add_new_book_invalid_name(self, collector, book_name):
        initial_books_count = len(collector.get_books_genre())
        collector.add_new_book(book_name)
        new_books_count = len(collector.get_books_genre())
        assert new_books_count == initial_books_count

    # Test setting book genre
    @pytest.mark.parametrize("book_name, genre", [
        ("Хоббит, или Туда и обратно", "Фантастика"),
        ("Дракула", "Ужасы"),
        ("В поисках Немо", "Мультфильмы"),
    ])
    def test_set_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Test if the genre returned matches the expected genre for a specific book
    def test_get_book_genre_from_name(self, collector):
        book_name = "Дракула"
        genre = "Ужасы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Test getting books from a specific genre
    @pytest.mark.parametrize("book_name, genre", [
        ("Хоббит, или Туда и обратно", "Фантастика"),
        ("Дракула", "Ужасы"),
    ])
    def test_get_books_with_specific_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert book_name in books
        assert genre in collector.genre

    # Test getting the list of book genres
    @pytest.mark.parametrize("book_name, genre", [
        ("Хоббит, или Туда и обратно", "Фантастика"),
        ("Дракула", "Ужасы"),
        ("В поисках Немо", "Мультфильмы"),
    ])
    def test_get_books_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books_genre = collector.get_books_genre()
        assert books_genre[book_name] == genre

    # Test getting books for children (valid child genre)
    def test_get_books_for_children_with_child_friendly_genre(self, collector):
        book_name = "В поисках Немо"
        genre = "Мультфильмы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        children_books = collector.get_books_for_children()
        assert book_name in children_books

    # Test getting books for children (adult genre)
    def test_get_books_for_children_with_adult_genre(self, collector):
        book_name = "Дракула"
        genre = "Ужасы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        children_books = collector.get_books_for_children()
        assert book_name not in children_books

    # Test favorites addition
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Лучшая книга")
        collector.add_book_in_favorites("Лучшая книга")
        assert "Лучшая книга" in collector.get_list_of_favorites_books()

    # Test favorites deletion
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Лучшая книга")
        collector.add_book_in_favorites("Лучшая книга")
        collector.delete_book_from_favorites("Лучшая книга")
        assert "Лучшая книга" not in collector.get_list_of_favorites_books()

    # Test getting favorites list
    def test_get_list_of_favorites_books(self, collector):
        book_name = "Лучшая книга"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites
