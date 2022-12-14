# Generated by Django 4.1.3 on 2022-12-05 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0009_alter_pokemons_legendary_alter_pokemons_second_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='second_type',
            field=models.ForeignKey(blank=True, default=19, on_delete=django.db.models.deletion.CASCADE, to='pokedex.second_type'),
        ),
        migrations.AlterField(
            model_name='pokemons',
            name='type',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='pokedex.type'),
        ),
    ]
