from django.contrib import admin

from NewsHub.models import WorldData, UserClass
from CLSGGameLogin.models import SimulationGame

# Register your models here.
admin.site.register(
    WorldData
)

admin.site.register(
    UserClass
)

admin.site.register(
    SimulationGame
)
