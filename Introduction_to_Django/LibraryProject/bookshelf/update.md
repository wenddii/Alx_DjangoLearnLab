# Update Book Instance

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book we want to update
book = Book.objects.get(title="1984")  # fetch the book with the original title

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(f"ID: {updated_book.id}, Title: {updated_book.title}, Author: {updated_book.author}, Year: {updated_book.publication_year}")
