import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.library_facade import LibraryFacade
from core.library_mediator import LibraryMediator
from core.user import StudentUserType, TeacherUserType

# Inicializar Mediator e Facade
mediator = LibraryMediator()
library = LibraryFacade(mediator)

# Adicionar usuários
student = StudentUserType(user_id=1, name="Alice")
teacher = TeacherUserType(user_id=2, name="Professor Bob")
mediator.add_user(student)
mediator.add_user(teacher)

# Adicionar livros ao mediador
mediator.add_book({"id": 1, "title": "Python Programming", "author": "John Doe", "category": "Programming", "available": True})
mediator.add_book({"id": 2, "title": "Data Structures", "author": "Jane Smith", "category": "Computer Science", "available": True})

# Buscar Livros
resultados_busca = library.search_books("Python")
print(resultados_busca)

# Empréstimo de Livro
emprestimo_sucesso = library.borrow_book(user_id=1, book_id=1)
print(f"Empréstimo realizado: {emprestimo_sucesso}")

# Verificar status do livro após o empréstimo
print(mediator.books[1])

# Devolução de Livro
devolucao_sucesso = library.return_book(user_id=1, book_id=1)
print(f"Devolução realizada: {devolucao_sucesso}")

# Verificar status do livro após a devolução
print(mediator.books[1])
