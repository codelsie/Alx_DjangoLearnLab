from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<Book: Book object (1)>from bookshelf.models import Book
books = Book.objects.all()
books
<QuerySet [<Book: Book object (1)>]>
books[0].title       
'1984'
book[0].author      
'George Orwell'
book[0].publication_year  
'1949'
from myapp.models import Book
books = Book.objects.all()
book = books[0]
book.title = "Nineteen Eighty-Four"
book.save()
book.title
'Nineteen Eighty-Four'
from myapp.models import Book
books = Book.objects.all()
book = books[0]
book.delete()
(1, {'bookshelf.Book': 1})

books
# <QuerySet []>
