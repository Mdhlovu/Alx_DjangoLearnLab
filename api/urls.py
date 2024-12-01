from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),
]


from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('token/', obtain_auth_token, name='api-token'),
]

