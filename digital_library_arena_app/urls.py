from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('languages/', views.languages, name='languages'),
    path('books/', views.books, name='books'),
    path('audio-books/', views.audio_books, name='audio_books'),
    path('academic/', views.academic, name='academic'),
]
