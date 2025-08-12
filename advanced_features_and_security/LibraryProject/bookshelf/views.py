from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Permissions and Groups:
# Groups:
#   - Viewers: can_view
#   - Editors: can_view, can_create, can_edit
#   - Admins: can_view, can_create, can_edit, can_delete
#
# These are enforced in views using the @permission_required decorator.
# Users are assigned to groups in Django admin.

@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/view_books.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    # Logic for creating a book
    pass

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic for editing a book
    pass

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Logic for deleting a book
    pass
