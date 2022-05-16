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
    xinzengyisi = models.IntegerField()
