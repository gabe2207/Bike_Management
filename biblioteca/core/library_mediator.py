from adapters.external_catalog_adapter import ExternalCatalogAdapter
from core.notifications import BookAvailabilityNotifier
from core.handlers import BookAvailabilityHandler, UserEligibilityHandler, LoanLimitHandler

class LibraryMediator:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.catalog_adapter = ExternalCatalogAdapter()
        self.notifier = BookAvailabilityNotifier()

    def add_user(self, user):
        self.users[user.user_id] = user

    def add_book(self, book):
        self.books[book['id']] = book

    def search_books(self, query):
        return self.catalog_adapter.search_books(query)

    def borrow_book(self, user_id, book_id):
        user = self.users.get(user_id)
        book = self.books.get(book_id)
        
        request = {'user': user, 'book': book}
        handler_chain = BookAvailabilityHandler()
        if handler_chain.handle(request, next_handler=UserEligibilityHandler()):
            if LoanLimitHandler().handle(request):
                if book and book['available']:
                    user.borrow_book(book)
                    book['available'] = False
                    self.notifier.notify(user, book)
                    return True
        return False

    def return_book(self, user_id, book_id):
        user = self.users.get(user_id)
        book = self.books.get(book_id)
        if book and book in user.loaned_books:
            user.return_book(book)
            book['available'] = True
            return True
        return False
