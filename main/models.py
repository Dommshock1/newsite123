from django.db import models

class Category(models.Model):
    title = models.CharField('Наименование', max_length=200)
    description = models.TextField('Описание товара')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField('Наименование', max_length=200)
    description = models.TextField('Описание товара')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title