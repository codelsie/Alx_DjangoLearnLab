import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# All books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name) 
books_by_author = Book.objects.filter(author=author) 

# List all books in a library 
library_name = "Central Library"
library = Library.objects.get(name=library_name)

for book in library.books.all():
    print(f" - {book.title}")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)