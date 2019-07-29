from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.name


class Book (models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img', blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=7)
    discount = models.DecimalField(decimal_places=2, max_digits=5)
    net_price = models.DecimalField(decimal_places=2, max_digits=7)
    #recomended = models.BooleanField(null=True, default=False)

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.title
