from myapp.models import Book
books = Book.objects.all()
book = books[0]
book.delete()
(1, {'bookshelf.Book': 1})

books
# <QuerySet []>
