from django.shortcuts import render
from CLSGGameLogin.models import SimulationGame


# Create your views here.
def index(request):
    """
    Displays the list of all games
    """
    if request.user.is_authenticated:
        allowed_games = request.user.allowed_games
    else:
        allowed_games = []
    games_list = SimulationGame.objects.all().order_by('-is_active',
                                                       'game_order')

    return render(request,
                  "Games/index.html",
                  {
                      'games': games_list,
                      'allowed_games': allowed_games,
                  })
