class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.loaned_books = []

    def borrow_book(self, book):
        self.loaned_books.append(book)

    def return_book(self, book):
        self.loaned_books.remove(book)

class StudentUserType(User):
    pass

class TeacherUserType(User):
    pass
