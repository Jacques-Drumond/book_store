from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })

def book_detail(request, slug):
    actual_book = get_object_or_404(Book, slug=slug)
    return render(request,  "book_outlet/book_detail.html", {
    "title": actual_book.title,
    "author": actual_book.author,
    "rating": actual_book.rating,
    "is_best_selling": actual_book.is_best_selling
    })