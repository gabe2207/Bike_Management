from core.user import User

class BookAvailabilityHandler:
    def handle(self, request, next_handler=None):
        if request['book']['available']:
            if next_handler:
                return next_handler.handle(request)
            return True
        return False

class UserEligibilityHandler:
    def handle(self, request, next_handler=None):
        if request['user'] and isinstance(request['user'], User):
            if next_handler:
                return next_handler.handle(request)
            return True
        return False

class LoanLimitHandler:
    def handle(self, request, next_handler=None):
        if len(request['user'].loaned_books) < 5:  # Supondo que o limite seja 5 livros
            if next_handler:
                return next_handler.handle(request)
            return True
        return False
