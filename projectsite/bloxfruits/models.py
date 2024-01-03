from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BloxFruit(BaseModel):
    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Legendary', 'Legandary'),
        ('Mythical', 'Mythical'),
    )
    TYPE_CHOICES = (
        ('Natural', 'Natural'),
        ('Elemental', 'Elemental'),
        ('Beast', 'Beast'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    rarity = models.CharField(max_length=100, null=True, blank=True, choices=RARITY_CHOICES)
    fruit_type = models.CharField(max_length=100, null=True, blank=True, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

class FightingStyle(BaseModel):
    LOCATION_CHOICES = (
        ('First Sea', 'First Sea'),
        ('Second Sea', 'Second Sea'),
        ('Third Sea', 'Third Sea'),
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True, choices=LOCATION_CHOICES)

    def __str__(self):
        return self.name

class Sword(BaseModel):
    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Legendary', 'Legandary'),
        ('Mythical', 'Mythical')
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    rarity = models.CharField(max_length=100, null=True, blank=True, choices=RARITY_CHOICES)

    def __str__(self):
        return self.name

class Gun(BaseModel):
    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Legendary', 'Legandary'),
        ('Mythical', 'Mythical')
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    rarity = models.CharField(max_length=100, null=True, blank=True, choices=RARITY_CHOICES)

    def __str__(self):
        return self.name

class Player(BaseModel):
    PLAYER_TYPE_CHOICES = (
        ('Pirate', 'Pirate'),
        ('Marine', 'Marine')
    ) 
    name = models.CharField(max_length=100, null=True, blank=True)
    player_type = models.CharField(max_length=100, null=True, blank=True, choices=PLAYER_TYPE_CHOICES)
    bloxfruit = models.ForeignKey(BloxFruit, blank=True, on_delete=models.CASCADE, null=True)
    fightingstyle = models.ManyToManyField(FightingStyle, blank=True)
    sword = models.ManyToManyField(Sword, blank=True)
    gun = models.ManyToManyField(Gun, blank=True)



