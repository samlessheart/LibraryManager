from django.contrib import admin
from .models import Book, PassBook, Author
# Register your models here.

admin.site.register(Book)
admin.site.register(PassBook)
admin.site.register(Author)


