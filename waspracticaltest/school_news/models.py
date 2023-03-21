from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=64, unique=True)
    author = models.CharField(max_length=128)
    date = models.DateField()
    text = models.CharField(max_length=512)

    class Meta:
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.title