from django.db import models

# Create your models here.

# ProductInfo describes the information about a particular product.
class ProductInfo(models.Model):
    name                = models.CharField(max_length=250)
    price               = models.DecimalField(max_digits=10, decimal_places=2)
    description         = models.CharField(max_length=250)
    quantity            = models.IntegerField() 
    is_available        = models.BooleanField(default=False, blank=False, null=False)


    class Meta:
        verbose_name = 'productInfo'
        verbose_name_plural = 'productInfo'


    def __str__(self):
        return f'{self.product_name}'

