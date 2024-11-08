**Command**:
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

1984 George Orwell 1949


retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

Nineteen Eighty-Four


retrieved_book.delete()
Book.objects.all()

(1, {'bookshelf.Book': 1})
<QuerySet []>




