from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=36)
    description = models.TextField(max_length=300)
    country = models.CharField(max_length=30, default='')
    genre = models.TextField(max_length=300, default='')
    year = models.IntegerField(null=True)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
            if len(ratings) > 0:
                return sum
            else:
                return 0

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))

class Actor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    movie = models.ManyToManyField(Movie, related_name='actors')

class Producer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    movie = models.ManyToManyField(Movie, related_name='producers')



