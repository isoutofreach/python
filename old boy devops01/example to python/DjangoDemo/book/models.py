from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32,unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()
    class Meta():
        db_table = "book"