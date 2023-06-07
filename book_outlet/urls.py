from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name="book-detail")
]
