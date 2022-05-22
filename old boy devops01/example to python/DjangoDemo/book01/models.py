from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()

    # 一对多的关联字段 publish_id
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE, db_constraint=False)

    # 多对多关系: 不会创建字段,会创建第三张表
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
