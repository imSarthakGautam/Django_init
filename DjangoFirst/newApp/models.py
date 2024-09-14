from django.db import models
from django.utils import timezone

# Create your models here.

class userModel(models.Model):

    #enums: to give fixed choices.
    GENDER = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHERS'),
    ]
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='imgModel/')
    # when you upload img Django will save in folder imgModel
    # install Pillow

    date_added = models.DateTimeField(default=timezone.now)
    sex=models.CharField(max_length=1, choices=GENDER)
    description= models.TextField(default='')

    def __str__(self):
        # to name userModel by own name, for sarthak data, it'll be known from name sarthak
        return self.name

#dJANGO RELATIONSHIPS: players, club country, fantasy team and stat relationships


# Club Model - Many-to-One with Player
class Club(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# NationalTeam Model - Many-to-One with Player
class NationalTeam(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# FantasyTeam Model - Many-to-Many with Player
class FantasyTeam(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField('Player', related_name='fantasy_teams')

    def __str__(self):
        return self.name

# Player Model
class Player(models.Model):
    # Position choices for the player
    POSITION_CHOICES = [
        ('MID', 'Midfielder'),
        ('FOR', 'Forward'),
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')  # Many-to-One Relationship
    national_team = models.ForeignKey(NationalTeam, on_delete=models.CASCADE, related_name='players_nt')  # Many-to-One Relationship
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)  # Position field with choices
    date_of_joining = models.DateField(default=timezone.now)  # Date of joining with default to current date

    def __str__(self):
        return self.name

# Statistics Model - One-to-One with Player
class Statistics(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='statistics')  # One-to-One Relationship
    goals = models.IntegerField()
    assists = models.IntegerField()
    matches = models.IntegerField()

    def __str__(self):
        return f'Statistics for {self.player.name}'
