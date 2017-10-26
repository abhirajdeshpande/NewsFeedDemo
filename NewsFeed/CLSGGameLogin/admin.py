from django.contrib import admin
from CLSGGameLogin.models import SimulationGame


# Register your models here.
class SimulationGameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'game_order', 'game_link', 'is_active')


admin.site.register(
    SimulationGame,
    SimulationGameAdmin
)
