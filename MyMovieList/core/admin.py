from django.contrib import admin
from core.models import *


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ["name"]
    exclude = ('version',)


@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display = ["name"]
    exclude = ('version',)


@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    list_display = ["title", "release_date"]
    exclude = ('version',)