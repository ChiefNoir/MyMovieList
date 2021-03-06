# Generated by Django 2.0.4 on 2018-04-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('version', models.PositiveIntegerField(default=0, verbose_name='Version')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('runtime', models.PositiveIntegerField(blank=True, null=True, verbose_name='Runtime (minutes)')),
                ('version', models.PositiveIntegerField(default=0, verbose_name='Version')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('version', models.PositiveIntegerField(default=0, verbose_name='Version')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(to='core.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='core.Genre'),
        ),
    ]
