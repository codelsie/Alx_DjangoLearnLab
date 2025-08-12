import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# All books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name) 
books_by_author = Book.objects.filter(author=author) 

print(f"Books by {author_name}:")
if books_by_author.exists():
    for book in books_by_author:
        print(f" - {book.title}")

# List all books in a library 
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    if library.books.exists():
        for book in library.books.all():
            print(f" - {book.title}")
    else:
        print("No books in this library.")
except Library.DoesNotExist:
    print(f"\nLibrary '{library_name}' not found.")


# Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"\nLibrary '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"\nNo librarian assigned to {library_name}.")
