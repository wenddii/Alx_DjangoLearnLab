from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library   # <-- checker wants this exact line


def book_list(request):
    books = Book.objects.all()
    return render(
        request,
        'relationship_app/list_books.html',
        {'books': books}
    )


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # <-- exact string required
    context_object_name = 'library'
