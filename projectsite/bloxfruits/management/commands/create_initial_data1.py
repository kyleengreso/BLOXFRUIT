from django.core.management.base import BaseCommand
from bloxfruits.models import FightingStyle

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_fighting_style()
        # self.create_sword()
        # self.create_gun()

    def create_fighting_style(self):
        fighting_style1 = FightingStyle(name='Combat', source='N/A', location='First Sea')
        fighting_style2 = FightingStyle(name='Dark Step', source='Dark Step Teacher', location='First Sea')
        fighting_style3 = FightingStyle(name='Electric', source='Mad Scienties', location='First Sea')
        fighting_style4 = FightingStyle(name='Water Kung Fu', source='Water Kung Fu Teacher', location='First Sea')
        fighting_style5 = FightingStyle(name='Dragon Breath', source='Sabi', location='Second Sea')
        fighting_style6 = FightingStyle(name='SuperHuman', source='Martial Arts Teacher', location='Second Sea')
        fighting_style7 = FightingStyle(name='Death Step', source='Phoeyu, the Reformed', location='Second Sea')
        fighting_style8 = FightingStyle(name='Sharkman Karate', source='Daigrock, the Sharkman ', location='SecondSea')
        fighting_style9 = FightingStyle(name='Electric Claw', source='Previous Hero', location='Third Sea')
        fighting_style10 = FightingStyle(name='Dragon Talon', source='Uzoth', location='Third Sea')
        fighting_style11 = FightingStyle(name='GodHuman', source='Ancient Monk', location='Third Sea')
        fighting_style12 = FightingStyle(name='Sanguine Art', source='Shafi', location='Third Sea')
        

        blox_fruit = [fighting_style1, fighting_style2, fighting_style3, fighting_style4, fighting_style5, fighting_style6, fighting_style7, fighting_style8, fighting_style9, fighting_style10, fighting_style11, fighting12]
        for fighting_style in blox_fruit:
            fighting_style.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully created Fighting Styles'))


