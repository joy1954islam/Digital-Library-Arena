from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def languages(request):
    return render(request, 'languages.html')


def books(request):
    return render(request, 'books.html')


def audio_books(request):
    return render(request, 'audio_books.html')


def academic(request):
    return render(request, 'academic.html')


def university(request):
    return render(request, 'university.html')


def newspapers(request):
    return render(request, 'newspapers.html')


def journals_and_magazine(request):
    return render(request, 'journals_and_magazine.html')


def digital_library_arena(request):
    return render(request, 'digital_library_arena.html')


def development(request):
    return render(request, 'development.html')


def enclyopedia(request):
    return render(request, 'enclyopedia.html')


def research(request):
    return render(request, 'research.html')


def kids(request):
    return render(request, 'kids.html')


def translation_and_language(request):
    return render(request, 'translation_and_language.html')


def login(request):
    return render(request, 'login.html')

