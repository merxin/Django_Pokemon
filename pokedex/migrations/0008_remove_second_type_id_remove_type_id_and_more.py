# Generated by Django 4.1.3 on 2022-12-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0007_remove_pokemons_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='second_type',
            name='id',
        ),
        migrations.RemoveField(
            model_name='type',
            name='id',
        ),
        migrations.AlterField(
            model_name='second_type',
            name='name',
            field=models.TextField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.TextField(blank=True, primary_key=True, serialize=False),
        ),
    ]