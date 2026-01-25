from django.db import models

class House(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    rooms = models.PositiveIntegerField()

    def __str__(self):
        return self.title
