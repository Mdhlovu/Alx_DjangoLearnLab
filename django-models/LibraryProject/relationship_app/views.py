from django.shortcuts import render
from .models import Book

from django.views.generic.detail import DetailView
from .models import Library

from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import permission_required

from django.contrib.auth.views import LoginView, LogoutView
from djoango.urls import reverse_lazy

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


#class view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'


def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


@permission_required('relationship_app.can_add_book')
def add_book(request):

