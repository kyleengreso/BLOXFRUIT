from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),

    path('blox-fruit', views.BloxFruitListView.as_view(), name='blox-fruit'),
    path('fighting-style', views.FightingStyleListView.as_view(), name='fighting-style'),
    path('sword', views.SwordListView.as_view(), name='sword'),
    path('gun', views.GunListView.as_view(), name='gun'),

    path('player', views.PlayerListView.as_view(), name='player'),
    path('player/add', views.PlayerCreateView.as_view(), name='player-add'),
    path('player/<pk>', views.PlayerUpdateView.as_view(), name='player-edit'),
    path('player/<pk>/delete', views.PlayerDeleteView.as_view(), name='player-del')

]