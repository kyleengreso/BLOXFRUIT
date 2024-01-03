from django.core.management.base import BaseCommand
from bloxfruits.models import Sword

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_sword()
        # self.create_gun()

    def create_sword(self):
        sword1 = Sword(name='Cutlass', rarity='Common')
        sword2 = Sword(name='Dual Katana', rarity='Common')
        sword3 = Sword(name='Katana', rarity='Common')
        sword4 = Sword(name='Iron Mace', rarity='Uncommon')
        sword5 = Sword(name='Shark Saw', rarity='Uncommon')
        sword6 = Sword(name='Triple Katana', rarity='Uncommon')
        sword7 = Sword(name='Twin Hooks', rarity='Uncommon')
        sword8 = Sword(name='Dragon Trident', rarity='Uncommon')
        sword9 = Sword(name='Dual-Headed Blade', rarity='Uncommon')
        sword10 = Sword(name='Gravity Cane', rarity='Uncommon')
        sword11 = Sword(name='Jitte', rarity='Uncommon')
        sword12 = Sword(name='Longsword', rarity='Uncommon')
        sword13 = Sword(name='Pipe', rarity='Uncommon')
        sword14 = Sword(name='Soul Cane', rarity='Uncommon')
        sword15 = Sword(name='Trident', rarity='Uncommon')
        sword16 = Sword(name='Wardens Sword', rarity='Uncommon')
        sword17 = Sword(name='Bisento', rarity='Legendary')
        sword18 = Sword(name='Buddy Sword', rarity='Legendary')
        sword19 = Sword(name='Carvander', rarity='Legendary')
        sword20 = Sword(name='Dark Dagger', rarity='Legendary')
        sword21 = Sword(name='Fox Lamp', rarity='Legendary')
        sword22 = Sword(name='Koko', rarity='Legendary')
        sword23 = Sword(name='Midnight Blade', rarity='Legendary')
        sword24 = Sword(name='Pole (1st Form)', rarity='Legendary')
        sword25 = Sword(name='Pole (2nd Form)', rarity='Legendary')
        sword26 = Sword(name='Renguko', rarity='Legendary')
        sword27 = Sword(name='Saber', rarity='Legendary')
        sword28 = Sword(name='Saddi', rarity='Legendary')
        sword29 = Sword(name='Shark Anchor', rarity='Legendary')
        sword30 = Sword(name='Shisui', rarity='Legendary')
        sword31 = Sword(name='Spikey Trident', rarity='Legendary')
        sword32 = Sword(name='Tushita', rarity='Legendary')
        sword33 = Sword(name='Wando', rarity='Legendary')
        sword34 = Sword(name='Yama', rarity='Legendary')
        sword35 = Sword(name='Cursed Dual Katana', rarity='Mythical')
        sword36 = Sword(name='Dark blade', rarity='Mythical')
        sword37 = Sword(name='Hallow Scythe', rarity='Mythical')
        sword38 = Sword(name='Triple Dark Blade', rarity='Mythical')
        sword39 = Sword(name='True Tripla Katana', rarity='Mythical')

        sword = [sword1, sword2, sword3, sword4, sword5, sword6, sword7, sword8, sword9, sword10, sword11, sword12, sword13, sword14, sword15, sword16, sword17, sword18, sword19, sword20, sword21, sword22, sword23, sword24, sword25, sword26, sword27, sword28, sword29, sword30, sword31, sword32, sword33, sword34, sword35, sword36, sword37, sword38, sword39 ]
        for sword in sword:
            sword.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully created Swords'))


