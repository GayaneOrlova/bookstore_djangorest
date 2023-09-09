from rest_framework import serializers

from books.models import Book
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # book = serializers.ForeignKey(Book)
    # quantity = serializers.PositiveIntegerField()
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # total_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # class Meta:
    #     model = Cart
    #     fields = "__all__"





