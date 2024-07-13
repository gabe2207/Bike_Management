class BookAvailabilityNotifier:
    def notify(self, user, book):
        print(f"Notificação: {user.name}, o livro '{book['title']}' está disponível.")
