from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def languages(request):
    return render(request, 'languages.html')


def books(request):
    return render(request, 'books.html')


def audio_books(request):
    return render(request, 'audio_books.html')
