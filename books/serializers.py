from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    title=serializers.CharField()
    author=serializers.CharField()
    created_at=serializers.DateField()
    price=serializers.FloatField()
    available = serializers.BooleanField(default=True)
    image = serializers.ImageField()
    rating = serializers.IntegerField()


