from django.db import models


class SlotType(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.name}'


class Slot(models.Model):
    class Meta:
        ordering = ['order']

    name = models.CharField(max_length=16)
    slot_type = models.ForeignKey(SlotType, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
