from rest_framework import serializers

from books.models import Book
from books.models import Genre

class BookSerializer(serializers.ModelSerializer):
    title=serializers.CharField()
    author=serializers.CharField()
    genre=serializers.SerializerMethodField(Genre) 
    created_at=serializers.DateField()
    price=serializers.FloatField()
    available = serializers.BooleanField(default=True)
    image = serializers.ImageField()
    rating = serializers.IntegerField()
    class Meta:
        model = Book
        fields = "__all__"
class GenreSerializer(serializers.ModelSerializer):
    name=serializers.CharField()




