from bookshelf.models import Book
books = Book.objects.all()
books
<QuerySet [<Book: Book object (1)>]>
books[0].title       
'1984'
book[0].author      
'George Orwell'
book[0].publication_year  
'1949'
