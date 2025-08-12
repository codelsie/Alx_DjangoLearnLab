from myapp.models import Book
books = Book.objects.all()
book = books[0]
book.title = "Nineteen Eighty-Four"
book.save()
book.title
'Nineteen Eighty-Four'
