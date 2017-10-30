from django.db import models


# Create your models here.
class SimulationGame(models.Model):
    game_order = models.IntegerField(blank=True)
    game_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/media')
    summary = models.CharField(max_length=1024)
    details = models.CharField(max_length=5120, blank=True)
    game_link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.game_name
