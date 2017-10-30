from django.http import Http404
from django.shortcuts import render
from CLSGGameLogin.models import SimulationGame

YES_CAN_PLAY = 1
NO_CANT_PLAY = 2
LOGIN_TO_CHECK = 3


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


def simulation(request):
    if request.method == 'GET':
        game_name = request.GET.get('game_name')
        try:
            game_info = SimulationGame.objects.get(game_name=game_name)

            if request.user.is_authenticated:
                if game_info.game_name in request.user.allowed_games:
                    can_play = YES_CAN_PLAY
                else:
                    can_play = NO_CANT_PLAY
            else:
                can_play = LOGIN_TO_CHECK

        except SimulationGame.DoesNotExist:
            raise Http404('No such game available!')

        return render(request,
                      'Games/game_index.html',
                      {
                          'game': game_info,
                          'can_play': can_play,
                          'YES_CAN_PLAY': YES_CAN_PLAY,
                          'NO_CANT_PLAY': NO_CANT_PLAY,
                          'LOGIN_TO_CHECK': LOGIN_TO_CHECK,
                      }
                      )
    else:
        raise Http404('Cannot access game!')
