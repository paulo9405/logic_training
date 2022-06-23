from django.db import models


class Double(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

    def save(self, *args, **kwargs):
        self.value = self.value * 2

        return super(Double, self).save(*args, **kwargs)