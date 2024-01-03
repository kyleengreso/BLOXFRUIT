from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BloxFruit, FightingStyle, Sword, Gun, Player
from .forms import PlayerForm
import json

from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    def get(self, request):
        return render(request, 'home.html', {})

class BloxFruitListView(ListView):
    model = BloxFruit
    template_name = 'blox-fruit.html'
    context_object_name = 'blox-fruits'
    json_file_path = 'data/bloxfruit_data.json'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bloxfruit_data = self.get_bloxfruit_data()
        context['bloxfruit_data'] = bloxfruit_data
        return context

    def get_bloxfruit_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('bloxfruit', [])

class FightingStyleListView(ListView):
    model = FightingStyle
    template_name = 'fighting-style.html'
    context_object_name = 'fighting-styles'
    json_file_path = 'data/fightingstyle_data.json'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fightingstyle_data = self.get_fightingstyle_data()
        context['fightingstyle_data'] = fightingstyle_data
        return context

    def get_fightingstyle_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('fightingstyle', [])

class SwordListView(ListView):
    model = Sword
    template_name = 'sword.html'
    context_object_name = 'sword'
    json_file_path = 'data/sword_data.json'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sword_data = self.get_sword_data()
        context['sword_data'] = sword_data
        return context

    def get_sword_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('sword', [])

class GunListView(ListView):
    model = Gun
    template_name = 'gun.html'
    context_object_name = 'gun'
    json_file_path = 'data/gun_data.json'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gun_data = self.get_gun_data()
        context['gun_data'] = gun_data
        return context

    def get_gun_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('gun', [])
class PlayerListView(ListView):
    model = Player
    template_name = 'player.html'
    context_object_name = 'player'
    # json_file_path = 'data/gun_data.json'
    # paginate_by = 5

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player_add.html'
    success_url = reverse_lazy('player')

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player_edit.html'
    success_url = reverse_lazy('player')

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'player_del.html'
    success_url = reverse_lazy('player')