from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    page_number = models.IntegerField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_best_selling = models.BooleanField(default=False)    

    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} {self.page_number} from {self.author}, pages and {self.rating} rating"
    
