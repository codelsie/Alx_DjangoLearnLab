import os
import django

# --- Setup Django environment ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Change this
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# --- Query 1: All books by a specific author ---
author_name = "George Orwell"
books_by_author = Book.objects.filter(author__name=author_name)

print(f"Books by {author_name}:")
if books_by_author.exists():
    for book in books_by_author:
        print(f" - {book.title}")
else:
    print("No books found for this author.")


# --- Query 2: List all books in a library ---
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


# --- Query 3: Retrieve the librarian for a library ---
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"\nLibrary '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"\nNo librarian assigned to {library_name}.")
