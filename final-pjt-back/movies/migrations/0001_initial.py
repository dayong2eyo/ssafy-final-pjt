# Generated by Django 3.2.13 on 2022-11-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('poster_path', models.TextField()),
                ('backdrop_path', models.TextField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('actors', models.ManyToManyField(related_name='actor_movie', to='movies.Actor')),
                ('genre_ids', models.ManyToManyField(related_name='genre_movie', to='movies.Genre')),
            ],
        ),
    ]
