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
    def __str__(self):
        return self.name

class orders(models.Model):
    oid = models.DecimalField(max_digits=5,decimal_places=0,null=False)
    cart = models.TextField(null=False)
    user = models.TextField(null=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        oid1 = str(self.oid)
        return oid1
