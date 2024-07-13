import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from core.library_facade import LibraryFacade
from core.library_mediator import LibraryMediator
from core.user import StudentUserType, TeacherUserType

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.mediator = LibraryMediator()
        self.library = LibraryFacade(self.mediator)

        # Adicionar usuários
        self.student = StudentUserType(user_id=1, name="Alice")
        self.teacher = TeacherUserType(user_id=2, name="Professor Bob")
        self.mediator.add_user(self.student)
        self.mediator.add_user(self.teacher)

        # Adicionar livros ao mediador
        self.mediator.add_book({"id": 1, "title": "Python Programming", "author": "John Doe", "category": "Programming", "available": True})
        self.mediator.add_book({"id": 2, "title": "Data Structures", "author": "Jane Smith", "category": "Computer Science", "available": True})

    def test_search_books(self):
        resultados_busca = self.library.search_books("Python")
        self.assertEqual(len(resultados_busca), 1)
        self.assertEqual(resultados_busca[0]['title'], "Python Programming")

    def test_borrow_book(self):
        emprestimo_sucesso = self.library.borrow_book(user_id=1, book_id=1)
        self.assertTrue(emprestimo_sucesso)
        self.assertFalse(self.mediator.books[1]['available'])

    def test_return_book(self):
        self.library.borrow_book(user_id=1, book_id=1)
        devolucao_sucesso = self.library.return_book(user_id=1, book_id=1)
        self.assertTrue(devolucao_sucesso)
        self.assertTrue(self.mediator.books[1]['available'])

if __name__ == '__main__':
    unittest.main()
