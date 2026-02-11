from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Example: Create some data
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")

    library1.books.set([book1, book3])  # Add books to library
    library2.books.set([book2])

    librarian1 = Librarian.objects.create(name="Alice", library=library1)
    librarian2 = Librarian.objects.create(name="Bob", library=library2)

    # 1️⃣ Query all books by a specific author
    jk_books = Book.objects.filter(author=author1)
    print("Books by J.K. Rowling:", [book.title for book in jk_books])

    # 2️⃣ List all books in a library
    central_books = library1.books.all()
    print("Books in Central Library:", [book.title for book in central_books])

    # 3️⃣ Retrieve the librarian for a library
    central_librarian = library1.librarian
    print("Librarian of Central Library:", central_librarian.name)

if __name__ == "__main__":
    import django
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
    django.setup()
    
    run_queries()
