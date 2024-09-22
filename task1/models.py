from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=1000000, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=100000, decimal_places=2)
    size = models.DecimalField(max_digits=1000000, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
