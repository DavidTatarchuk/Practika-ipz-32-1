from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_available = True

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    def __str__(self):
        status = "Доступна" if self.__is_available else "Видана"
        return f"Книга: '{self.title}' ({self.author}) [{status}]"

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_role(self):
        pass

class Reader(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def show_role(self):
        print(f"{self.name} — Читач бібліотеки")

    def receive_book(self, book):
        self.borrowed_books.append(book)

    def show_books(self):
        print(f"Книги у читача {self.name}:")
        for book in self.borrowed_books:
            print(f" - {book.title}")

class Librarian(Person):
    def show_role(self):
        print(f"{self.name} — Бібліотекар")

    def issue_book(self, book, reader):
        if book.borrow():
            reader.receive_book(book)
            print(f"Бібліотекар {self.name} видав книгу '{book.title}' читачу {reader.name}")
        else:
            print(f"Відмова: Книга '{book.title}' зараз недоступна")

book1 = Book("Кобзар", "Т. Шевченко")
book2 = Book("Тіні забутих предків", "М. Коцюбинський")

librarian = Librarian("Ольга Петрівна")
reader1 = Reader("Максим")
reader2 = Reader("Ірина")

people = [librarian, reader1, reader2]
for person in people:
    person.show_role()

print("-" * 30)

print(book1)
librarian.issue_book(book1, reader1)
print(book1)

print("-" * 30)

librarian.issue_book(book1, reader2)

print("-" * 30)
reader1.show_books()