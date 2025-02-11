from django.db import models

# Create your models here.

class DirectorModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя режиссера')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    experience = models.IntegerField(verbose_name='Опыт, количество лет')
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Стоимость за смену')
    foto = models.ImageField(upload_to='images/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name