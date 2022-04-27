from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=30)
    cost = models.IntegerField('Цена')
    image = models.ImageField(default='Default value')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkti'

class Comment(models.Model):
    author = models.CharField(max_length=30, default='Won\'t say who')
    picture = models.ImageField(default='Default value')
    title = models.CharField('Название', max_length=20)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Sell(models.Model):
    salesman = models.CharField(max_length=20, default='Salesman')
    buyer = models.CharField(max_length=20, default='Buyer')
    product = models.CharField(max_length=30, default='Something interesting')
    cost = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.product

class Post(models.Model):
    author = models.CharField(max_length=30, default='Won\'t say who')
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class Made_Page(models.Model):
    title = models.CharField(max_length=40, default="No title")
    content = models.TextField(blank=True)
    age = models.IntegerField(default='Default value')
    author = models.CharField(max_length=30, default='Won\'t say who')
    is_published = models.BooleanField(default=True, verbose_name='Public')
    background_color = models.CharField(max_length=30, default='white')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})