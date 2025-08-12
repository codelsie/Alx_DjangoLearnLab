from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import redirect
from .forms import ExampleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/view_books.html', {'books': books})

@require_http_methods(["GET", "POST"])
def search_books(request):
    form = ExampleForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            books = Book.objects.filter(title__icontains=q)
        else:
            books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})


@login_required
@require_http_methods(["POST"])
def create_book_minimal(request):
    title = request.POST.get('title', '').strip()
    author = request.POST.get('author', '').strip()
    if not title:
        return render(request, 'bookshelf/form_example.html', {'error': 'Title required'})
    Book.objects.create(title=title, author=author)
    return redirect('bookshelf:book_list') 
