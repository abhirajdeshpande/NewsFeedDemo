from django.shortcuts import render
from NewsHub.models import WorldNewsCenterClass


# Create your views here.
def index(request):
    """
    Root page view
    """
    worlds = WorldNewsCenterClass.objects.order_by("news_center_name")

    return render(request, "NewsFeed/index.html", {
        "worlds": worlds,
    })
