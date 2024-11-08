from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)

library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

librarian = Librarian.objects.get(library=library)
