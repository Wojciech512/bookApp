from django.db import models

# Create your models here.
class Book(models.Model):
    CATEGORY_CHOICES = (
        ('Thriller','Thriller'),
        ('Fantasy','Fantasy'),
        ('Novel','Novel'),

    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50 , choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title