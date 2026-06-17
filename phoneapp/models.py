from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    foundation = models.DateField(verbose_name='date foundation', null=True)
    website = models.URLField(max_length=350, blank=True, null=True)

    def __str__(self):
        return self.name

class Smartphone(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ram = models.IntegerField(help_text='en GB')
    memory_capacity = models.IntegerField(help_text='en GB')
    screen_size = models.DecimalField(max_digits=4, decimal_places=2, help_text='in inches', blank=True, null=True)

    def __str__(self):
        return f"{self.manufacturer.name} - {self.name}"