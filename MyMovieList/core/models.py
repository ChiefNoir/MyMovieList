from django.db import models

class Genre(models.Model):
    name = models.CharField('Name', max_length=255, blank=False, null=False)
    version = models.PositiveIntegerField('Version', blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Person(models.Model):
    name = models.CharField('Name', max_length=255, blank=False, null=False)
    bio = models.TextField('Description', blank=True, null=True)
    version = models.PositiveIntegerField('Version', blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Movie(models.Model):
    title = models.CharField('Title', max_length=255, blank=False, null=False)
    year = models.DateField('Release Date', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    runtime = models.PositiveIntegerField('Runtime (minutes)', blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    director = models.ManyToManyField(Person)
    version = models.PositiveIntegerField('Version', blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
