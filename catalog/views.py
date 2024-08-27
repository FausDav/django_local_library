from django.shortcuts import render
from .models import Book, Author, BookInstance

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_books_novels = Book.objects.filter(genre__name__icontains='Novela').count()
    num_books_night = Book.objects.filter(title__icontains='noche').count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_novels': num_books_novels,
        'num_books_night': num_books_night,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)