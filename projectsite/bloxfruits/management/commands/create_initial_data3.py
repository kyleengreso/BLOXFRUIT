from django.core.management.base import BaseCommand
from bloxfruits.models import Gun

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_gun()

    def create_gun(self):
        gun1 = Gun(name='Slingshot', rarity='Common')
        gun2 = Gun(name='Flintlock', rarity='Uncommon')
        gun3 = Gun(name='Musket', rarity='Uncommon')
        gun4 = Gun(name='Acidum Rifle', rarity='Uncommon')
        gun5 = Gun(name='Bizzare Rifle', rarity='Uncommon')
        gun6 = Gun(name='Cannon', rarity='Uncommon')
        gun7 = Gun(name='Refined Flintlock', rarity='Uncommon')
        gun8 = Gun(name='Refined Musket', rarity='Uncommon')
        gun9 = Gun(name='Refined Slingshot', rarity='Uncommon')
        gun10 = Gun(name='Bazooka', rarity='Legendary')
        gun11 = Gun(name='Kabucha', rarity='Legendary')
        gun12 = Gun(name='Serpent Bow', rarity='Legendary')
        gun13 = Gun(name='Soul Guitar', rarity='Mythical')

        gun = [gun1, gun2, gun3, gun4, gun5, gun6, gun7, gun8, gun9, gun10, gun11, gun12, gun13]
        for gun in gun:
            gun.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully created Guns'))
