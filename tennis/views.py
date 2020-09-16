from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from .models import Players

# Create your views here.

# players = [
#     {'id': 1, 'name': 'Roger Federer', 'age': 34},
#     {'id': 2, 'name': 'Rafael Nadal', 'age': 32},
#     {'id': 3, 'name': 'Novak Djokovic', 'age': 30}
# ]


def server_error(request):
    return HttpResponse("<h1>Nope</h1>")


def index(request):
    context = {'player': Players.objects.all()}
    return render(request, 'tennis/index.html', context)


@login_required
def show(request, player_id):
    context = {'player': Players.objects.get(pk=player_id)}
    return render(request, 'tennis/show.html', context)
