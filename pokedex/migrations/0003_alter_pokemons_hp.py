# Generated by Django 4.1.3 on 2022-12-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_second_type_options_alter_type_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='hp',
            field=models.PositiveIntegerField(default=1),
        ),
    ]