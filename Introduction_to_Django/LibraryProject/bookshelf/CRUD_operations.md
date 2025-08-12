from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<Book: Book object (1)>

from bookshelf.models import Book
Book.objects.get(title="1984")
<Book: Book object (1)>

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
'Nineteen Eighty-Four'

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.delete()
(1, {'bookshelf.Book': 1})

