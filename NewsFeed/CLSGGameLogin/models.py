from django.db import models


# Create your models here.
class SimulationGame(models.Model):
    game_order = models.IntegerField(blank=True)
    game_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/media')
    summary = models.CharField(max_length=1024)
    game_link = models.URLField(blank=True)

    def __str__(self):
        return self.game_name
