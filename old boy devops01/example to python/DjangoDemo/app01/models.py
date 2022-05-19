from django.db import models

# Create your models here.

# ORM
'''
create table t1(
    name varchar(32) unique not null 
    age int 
)
'''


class Ncov(models.Model):
    city = models.CharField(max_length=32, unique=True)
    xinzengyisi = models.IntegerField(default=0)
    xinzengquezhen = models.IntegerField(null=True)
    leijiquezhen = models.IntegerField(default=0)
    leijisiwang = models.IntegerField(default=0)
    #models.DecimalField(max_digits=8,decimal_places=2)   最大8位,可以小数点后面2位
    #models.DateTimeField()
    class Meta:
        db_table = 'ncov'