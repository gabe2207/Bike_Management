class ExternalCatalogAdapter:
    def __init__(self):
        self.catalog = [
            {"id": 1, "title": "Python Programming", "author": "John Doe", "category": "Programming"},
            {"id": 2, "title": "Data Structures", "author": "Jane Smith", "category": "Computer Science"},
            {"id": 3, "title": "Machine Learning", "author": "John Doe", "category": "Artificial Intelligence"},
        ]

    def search_books(self, query):
        return [book for book in self.catalog if query.lower() in book["title"].lower()]
