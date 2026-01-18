# Delete Book Instance

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book we want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")  # fetch the updated book

# Delete the book
book.delete()

# Verify deletion
books = Book.objects.all()
print(books)

#<QuerySet []>
