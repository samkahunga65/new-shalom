from django.db import models

class Ingredient(models.Model):
    ingredient = models.CharField(max_length=120)
    def __str__(self):
        return self.ingredient

class Dish(models.Model):
    item_name = models.CharField(max_length=120)
    price = models.IntegerField(editable=True, default=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.item_name} @ {self.price}'


