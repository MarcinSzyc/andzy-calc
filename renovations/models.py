from django.db import models

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


class Room(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.TextField()
    type = models.IntegerField(choices=ROOM_TYPE)
    width = models.FloatField()
    length = models.FloatField()
    height = models.FloatField()
    tiles_height = models.FloatField(blank=True)
    renovation = models.ForeignKey(Renovation, on_delete=models.DO_NOTHING, null=True, blank=True)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name


class Cost(models.Model):
    room = models.OneToOneField(Room, on_delete=models.DO_NOTHING)
    floor = models.IntegerField()
    walls = models.IntegerField()
    ceiling = models.IntegerField()
    tiles = models.IntegerField()
    addons = models.IntegerField()
    basic_sum = models.IntegerField()
    labor = models.IntegerField()
    total_sum = models.IntegerField()
