from django.db import models
from django.core.exceptions import ValidationError
from django.db import transaction
from .Genre import Genre
from .Person import Person


class Movie(models.Model):
    title = models.CharField('Title', max_length=255, blank=False, null=False)
    release_date = models.DateField('Release Date', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    runtime = models.PositiveIntegerField('Runtime (minutes)', blank=True, null=True)
    genres = models.ManyToManyField(Genre)
    director = models.ManyToManyField(Person)
    version = models.PositiveIntegerField('Version', blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


    def __str__(self):
        return f"{self.title} ({self.release_date.year})"


    @transaction.atomic
    def save(self, *args, **kwargs):
        stored = Movie.objects.filter(pk=self.pk).first()
        if (stored == None or stored.version == self.version):
            self.version += 1
            super(Movie, self).save(*args, **kwargs)
        else:
            raise ValidationError('The item has already changed by someone')