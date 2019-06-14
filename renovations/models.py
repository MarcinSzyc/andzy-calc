from django.db import models
from django.db.models.signals import post_save

PRODUCT_TYPE = (
    (1, "Armature"),
    (2, "Tiles"),
    (3, "Paint"),
    (4, "Floor"),
    (5, "Other"),
)

ROOM_TYPE = (
    (1, "Normal"),
    (2, "Bathroom"),
)


class Renovation(models.Model):
    name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=128, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.TextField()
    price = models.FloatField(default=0)
    type = models.IntegerField(choices=PRODUCT_TYPE)

    def __str__(self):
        return self.name


class Cost(models.Model):
    floor = models.FloatField(default=0)
    walls = models.FloatField(default=0)
    ceiling = models.FloatField(default=0)
    tiles = models.FloatField(default=0)
    addons = models.FloatField(default=0)
    basic_sum = models.FloatField(default=0)
    labor = models.FloatField(default=0)
    total_sum = models.FloatField(default=0)


class Room(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.TextField()
    type = models.IntegerField(choices=ROOM_TYPE)
    width = models.FloatField(default=0)
    length = models.FloatField(default=0)
    height = models.FloatField(default=0)
    tiles_height = models.FloatField(default=0, blank=True, null=True)
    renovation = models.ForeignKey(Renovation, on_delete=models.DO_NOTHING, null=True, blank=True)
    product = models.ManyToManyField(Product, blank=True)
    cost = models.OneToOneField(Cost, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
