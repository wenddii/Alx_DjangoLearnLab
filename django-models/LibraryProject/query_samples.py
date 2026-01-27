# query_samples.py
# Run this with: python manage.py shell < query_samples.py
# or import it in Django shell

import django
import os

# Setup Django environment so this script can run standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from .models import Author, Book, Library, Librarian

# ------------------------------
# 1️⃣ Query all books by a specific author
# ------------------------------
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

# ------------------------------
# 2️⃣ List all books in a library
# ------------------------------
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in library '{library.name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

# ------------------------------
# 3️⃣ Retrieve the librarian for a library
# ------------------------------
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarians = library.librarians.all()  # related_name="librarians"
        print(f"Librarians in '{library.name}':")
        for librarian in librarians:
            print(f"- {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

# ------------------------------
# Sample usage
# ------------------------------
if __name__ == "__main__":
    books_by_author("George Orwell")
    print()
    books_in_library("Central Library")
    print()
    librarian_for_library("Central Library")
