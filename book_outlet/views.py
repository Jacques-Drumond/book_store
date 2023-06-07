from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Max, Min
# Create your views here.

def index(request):

    books = Book.objects.all().order_by("title")
    total_num_of_books = books.count()
    avg_book_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": total_num_of_books,
        "average_rating": avg_book_rating.get("rating__avg")
    })

def book_detail(request, slug):
    actual_book = get_object_or_404(Book, slug=slug)
    return render(request,  "book_outlet/book_detail.html", {
    "title": actual_book.title,
    "author": actual_book.author,
    "rating": actual_book.rating,
    "is_best_selling": actual_book.is_best_selling
    })