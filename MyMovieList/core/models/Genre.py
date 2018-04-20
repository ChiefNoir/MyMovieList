from django.db import models
from django.core.exceptions import ValidationError
from django.db import transaction


class Genre(models.Model):
    name = models.CharField('Name', max_length=255, blank=False, null=False)
    version = models.PositiveIntegerField('Version', blank=False, null=False, default=0)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    @transaction.atomic
    def save(self, *args, **kwargs):
        stored = Genre.objects.filter(pk = self.pk).first()
        if (stored == None or stored.version == self.version):
            self.version += 1
            super(Genre, self).save(*args, **kwargs)
        else:
            raise ValidationError('The item has already changed by someone')

    def __str__(self):
        return '{name}'.format(name=self.name)