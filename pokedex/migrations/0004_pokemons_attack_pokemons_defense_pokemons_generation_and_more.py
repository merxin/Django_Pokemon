# Generated by Django 4.1.3 on 2022-12-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemons_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemons',
            name='attack',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemons',
            name='defense',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pokemons',
            name='generation',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='pokemons',
            name='legendary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pokemons',
            name='speed',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]