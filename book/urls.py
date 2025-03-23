from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.bookIndex, name='bookIndex'),
    path('addbook/', views.addBook, name='addBook'),
    path('updatebook/<int:book_id>/', views.updateBook, name='updateBook'), 
    path('deletebook/<int:book_id>/', views.deleteBook, name='deleteBook'),
]



