from django.contrib import admin
from books.models import Book
from books.models import Genre

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Genre)
admin.site.register(Book)


