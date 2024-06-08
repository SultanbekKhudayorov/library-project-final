from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (BookListAPIView, BookDetailAPIView, \
                    BookDeleteAPIView, BookUpdateAPIView, \
                    BookCreateAPIView, BookListCreateAPIView, \
                    BookUpdateDeleteAPIView, BookViewset)

router = SimpleRouter()
router.register('books', BookViewset, basename='books')


urlpatterns = [
    # path('books/', BookListAPIView.as_view()),
    # path('booklistcreate/', BookListCreateAPIView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteAPIView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view()),
    # path('books/<int:pk>/', BookDetailAPIView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
]

urlpatterns += router.urls