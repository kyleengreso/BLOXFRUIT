from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.BloxFruit)
class BloxFruitAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "fruit_type", "created_at", "updated_at")
    search_fields = ("name", "fruit_type")

@admin.register(models.FightingStyle)
class FightingStyleAdmin(admin.ModelAdmin):
    list_display = ("name", "source", "location", "created_at", "updated_at")
    search_fields = ("name", "location")

@admin.register(models.Sword)
class SwordAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "created_at", "updated_at")
    search_fields = ("name", "rarity")

@admin.register(models.Gun)
class GunAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "created_at", "updated_at")
    search_fields = ("name", "rarity")

@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "player_type", "created_at", "updated_at")
    search_fields = ('name', 'player_type')