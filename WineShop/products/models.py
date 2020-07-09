from django.db import models

# Create your models here.
class products(models.Model):
    price = models.DecimalField(max_digits=8,decimal_places=2,null=False)
    name = models.TextField(null=False)
    quantity = models.DecimalField(max_digits=4,decimal_places=0)
    categories = [
        ('beer', 'Beer'),
        ('whiskey', 'Whiskey'),
        ('wine', 'Wine'),
        ('vodka', 'Vodka'),
        ('spirits', 'Spirits'),
    ]
    category = models.CharField(
        max_length=7,
        choices=categories,
        default='beer',
    )
