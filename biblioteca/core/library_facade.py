class LibraryFacade:
    def __init__(self, mediator):
        self.mediator = mediator

    def search_books(self, query):
        return self.mediator.search_books(query)

    def borrow_book(self, user_id, book_id):
        return self.mediator.borrow_book(user_id, book_id)

    def return_book(self, user_id, book_id):
        return self.mediator.return_book(user_id, book_id)
