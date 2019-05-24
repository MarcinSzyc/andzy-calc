from django.db import models

TYPE = (
    (1, "Armature"),
    (2, "Tiles"),
    (3, "Paint"),
    (4, "Other"),
)


class Product(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE)
