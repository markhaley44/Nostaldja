from django.db import models


class Decades(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year


class Fads(models.Model):
    name = models.CharField(max_length=250)
    image_url = models.CharField(max_length=500)
    description = models.TextField()
    decade = models.ForeignKey(
        Decades, on_delete=models.CASCADE, default='', related_name='Decades')

    def __str__(self):
        return self.name
