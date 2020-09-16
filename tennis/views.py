from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

players = [
    {'id': 1, 'name': 'Roger Federer', 'age': 34},
    {'id': 2, 'name': 'Rafael Nadal', 'age': 32},
    {'id': 3, 'name': 'Novak Djokovic', 'age': 30}
]


def index(request):
    context = {'players': players}
    return render(request, 'tennis/index.html', context)


def show(request, player_id):
    context = {'player': players[player_id - 1]}
    return render(request, 'tennis/show.html', context)
