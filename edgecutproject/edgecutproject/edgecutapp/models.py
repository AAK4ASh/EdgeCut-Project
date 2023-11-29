from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField(blank=True)
    image=models.ImageField(upload_to='product')
    stock=models.IntegerField(default=0)

    class Meta:
        ordering=('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    def __str__(self):
         return self.name
     
    