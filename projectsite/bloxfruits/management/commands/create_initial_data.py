from django.core.management.base import BaseCommand
from bloxfruits.models import BloxFruit

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_blox_fruit()

    def create_blox_fruit(self):
        card1 = BloxFruit(name='Rocket', rarity='Common', fruit_type = 'Natural')
        card2 = BloxFruit(name='Spin', rarity='Common', fruit_type = 'Natural')
        card3 = BloxFruit(name='Chop', rarity='Common', fruit_type = 'Natural')
        card4 = BloxFruit(name='Spring', rarity='Common', fruit_type = 'Natural')
        card5 = BloxFruit(name='Bomb', rarity='Common', fruit_type = 'Natural')
        card6 = BloxFruit(name='Smoke', rarity='Common', fruit_type = 'Elemental')
        card7 = BloxFruit(name='Spike', rarity='Common', fruit_type = 'Natural')
        card8 = BloxFruit(name='Flame', rarity='Uncommon', fruit_type = 'Elemental')
        card9 = BloxFruit(name='Falcon', rarity='Uncommon', fruit_type = 'Beast')
        card10 = BloxFruit(name='Sand', rarity='Uncommon', fruit_type = 'Elemental')
        card11 = BloxFruit(name='Dark', rarity='Uncommon', fruit_type = 'Elemental')
        card12 = BloxFruit(name='Diamond', rarity='Uncommon', fruit_type = 'Natural')
        card13 = BloxFruit(name='Barrier', rarity='Uncommon', fruit_type = 'Natural')
        card14 = BloxFruit(name='Magma', rarity='Uncommon', fruit_type = 'Elemental')
        card15 = BloxFruit(name='Rubber', rarity='Uncommon', fruit_type = 'Natural')
        card16 = BloxFruit(name='Ghost', rarity='Uncommon', fruit_type = 'Natural')
        card17 = BloxFruit(name='Light', rarity='Uncommon', fruit_type = 'Elemental')
        card18 = BloxFruit(name='Ice', rarity='Uncommon', fruit_type = 'Elemental')
        card19 = BloxFruit(name='Quake', rarity='Legendary', fruit_type = 'Natural')
        card20 = BloxFruit(name='Buddah', rarity='Legendary', fruit_type = 'Beast')
        card21 = BloxFruit(name='Sound', rarity='Legendary', fruit_type = 'Natural')
        card22 = BloxFruit(name='Love', rarity='Legendary', fruit_type = 'Natural')
        card23 = BloxFruit(name='Spider', rarity='Legendary', fruit_type = 'Natural')
        card24 = BloxFruit(name='Phoenix', rarity='Legendary', fruit_type = 'Elemental')
        card25 = BloxFruit(name='Portal', rarity='Legendary', fruit_type = 'Natural')
        card26 = BloxFruit(name='Rumble', rarity='Legendary', fruit_type = 'Elemental')
        card27 = BloxFruit(name='Blizzard', rarity='Legendary', fruit_type = 'Elemental')
        card28 = BloxFruit(name='Pain', rarity='Legendary', fruit_type = 'Natural')
        card29 = BloxFruit(name='T-Rex', rarity='Mythical', fruit_type = 'Beast')
        card30 = BloxFruit(name='Dough', rarity='Mythical', fruit_type = 'Elemental')
        card31 = BloxFruit(name='Dragon', rarity='Mythical', fruit_type = 'Beast')
        card32 = BloxFruit(name='Gravity', rarity='Mythical', fruit_type = 'Natural')
        card33 = BloxFruit(name='Mammoth', rarity='Mythical', fruit_type = 'Beast')
        card34 = BloxFruit(name='Shadow', rarity='Mythical', fruit_type = 'Natural')
        card35 = BloxFruit(name='Venom', rarity='Mythical', fruit_type = 'Natural')
        card36 = BloxFruit(name='Control', rarity='Mythical', fruit_type = 'Natural')
        card37 = BloxFruit(name='Spirit', rarity='Mythical', fruit_type = 'Natural')
        card38 = BloxFruit(name='Leopard', rarity='Mythical', fruit_type = 'Beast')
        card39 = BloxFruit(name='Kitsune', rarity='Mythical', fruit_type = 'Beast')
        


        blox_fruit = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30, card31, card32, card33, card34, card35, card36, card37, card38, card39 ]
        for card in blox_fruit:
            card.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully created Blox Fruit Cards'))


