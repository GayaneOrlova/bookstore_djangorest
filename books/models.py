from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    price=models.FloatField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])


    # genre=models.ManyToManyField() # добавить ссылку на модель с жанрами
    # rating=models.FloatField(),
    
    def __str__(self):
        return self.title
        
    