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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_new_book_rating_is_1(self):
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 1')
        assert collector.get_book_rating('Книга с рейтингом 1') == 1

    # Тесты для метода set_book_rating
    def test_set_book_rating_rating_0_book_rating_is_1(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 0. Ожидаемый результат: рейтинг равен 1
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 0')
        collector.set_book_rating('Книга с рейтингом 0', 0)
        assert collector.get_book_rating('Книга с рейтингом 0') == 1

    def test_set_book_rating_rating_1_book_rating_is_1(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 1. Ожидаемый результат: рейтинг равен 1
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 1')
        collector.set_book_rating('Книга с рейтингом 1', 1)
        assert collector.get_book_rating('Книга с рейтингом 1') == 1

    def test_set_book_rating_rating_2_book_rating_is_2(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 2. Ожидаемый результат: рейтинг равен 2
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 2')
        collector.set_book_rating('Книга с рейтингом 2', 2)
        assert collector.get_book_rating('Книга с рейтингом 2') == 2

    def test_set_book_rating_rating_9_book_rating_is_9(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 9. Ожидаемый результат: рейтинг равен 9
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 9')
        collector.set_book_rating('Книга с рейтингом 9', 9)
        assert collector.get_book_rating('Книга с рейтингом 9') == 9

    def test_set_book_rating_rating_10_book_rating_is_10(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 10. Ожидаемый результат: рейтинг равен 10
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 10')
        collector.set_book_rating('Книга с рейтингом 10', 10)
        assert collector.get_book_rating('Книга с рейтингом 10') == 10

    def test_set_book_rating_set_book_rating_11_book_rating_is_1(self):
        """
        Проверка приграничного значения рейтинга. Попытка установить рейтинг = 11. Ожидаемый результат: рейтинг равен 1
        """
        collector = BooksCollector()
        collector.add_new_book('Книга с рейтингом 11')
        collector.set_book_rating('Книга с рейтингом 11', 11)
        assert collector.get_book_rating('Книга с рейтингом 11') == 1
