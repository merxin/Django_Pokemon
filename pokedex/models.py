from django.db import models
import csv

class Second_Type(models.Model):
    def __str__(self):
        return self.name

    name = models.TextField(blank=True, primary_key=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Second_Type"
        verbose_name_plural = "Second_Types"

class Type(models.Model):
    def __str__(self):
        return self.name

    name = models.TextField(blank=True, primary_key=True)
    description = models.TextField(blank=True)
    count_ = models.Count('name')

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"



class Pokemons(models.Model):

    def __str__(self):
        return self.name

    type = models.ForeignKey(Type, blank=True, on_delete=models.CASCADE,default=1, to_field='name')
    second_type = models.ForeignKey(Second_Type, blank=True, on_delete=models.CASCADE, to_field='name', default='no_type')
    name = models.CharField(max_length=100)
    hp = models.PositiveIntegerField(default=1)
    attack = models.PositiveIntegerField(default=1)
    defense = models.PositiveIntegerField(default=1)
    sp_attack = models.PositiveIntegerField(default=1)
    sp_defense = models.PositiveIntegerField(default=1)
    speed = models.PositiveIntegerField(default=1, blank=True)
    generation = models.PositiveIntegerField(default=1, blank=True)
    legendary = models.CharField(max_length=100)
    total = models.PositiveIntegerField(default=7)


    class Meta:
        ordering = ("-total",)
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"
# Create your models here.
