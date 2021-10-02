from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    date = models.DateTimeField(auto_now=True, verbose_name='Date')
    text = models.TextField(max_length=200, verbose_name='Text Field')
    category = models.ForeignKey('Category', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-date']

    def __str__(self):
        return f'{self.category}: {self.title}'


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
