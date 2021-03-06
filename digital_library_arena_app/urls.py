from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('languages/', views.languages, name='languages'),
    path('books/', views.books, name='books'),
    path('audio-books/', views.audio_books, name='audio_books'),
    path('academic/', views.academic, name='academic'),
    path('university/', views.university, name='university'),
    path('newspapers/', views.newspapers, name='newspapers'),
    path('journals_and_magazine', views.journals_and_magazine, name='journals_and_magazine'),
    path('digital_library_arena/', views.digital_library_arena, name='digital_library_arena'),
    path('development/', views.development, name='development'),
    path('enclyopedia/', views.enclyopedia, name='enclyopedia'),
    path('research/', views.research, name='research'),
    path('kids/', views.kids, name='kids'),
    path('translation_and_language/', views.translation_and_language, name='translation_and_language'),
    path('login/', views.login, name='login'),
]
