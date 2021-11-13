from django.db import models
# from django.db.models import models

# Create your models here.


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Comman(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.PositiveBigIntegerField(default=0)
    likes = models.PositiveBigIntegerField(null=True, default=0)
    poster = models.ImageField(upload_to='pinterest_posters', null=True)
    actors = models.ManyToManyField('Actor')
    categories = models.ManyToManyField('Category')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Movie(Comman):
    pass


class Series(Comman):
    pass
