from django.db import models

class genre(models.Model):
    name = models.CharField('Name', max_length=255, blank=False, null=False)

class movie(models.Model):
    title = models.CharField('Title', max_length=255, blank=False, null=False)
    year = models.DateField('Release Date', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    runtime = models.PositiveIntegerField('Runtime (minutes)', blank=True, null=True)
    genres = models.ManyToManyField(genre)
