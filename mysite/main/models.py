from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Club name', max_length=60)

    def __str__(self) -> str:
        return self.name

class Player(models.Model):

    club_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Player name', max_length=50)
    position = models.CharField('Position', max_length=20)
    image = models.ImageField('Player image', upload_to='media/players/')

    def __str__(self) -> str:
        return self.name


