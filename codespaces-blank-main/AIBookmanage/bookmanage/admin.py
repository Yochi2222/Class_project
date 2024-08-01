from django.contrib import admin

# Import the Book model from the models.py file
from .models import Book

# Register the Book model with the admin site
admin.site.register(Book)