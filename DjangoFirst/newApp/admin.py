from django.contrib import admin
from .models import userModel, Player, Club, NationalTeam, Statistics, FantasyTeam


# Register your models here.

# Inline class to display Player instances in the Club admin
class PlayerInline(admin.TabularInline):  # Use StackedInline for a stacked layout
    model = Player
    extra = 1  # Number of extra forms to display
    fields = ['name', 'position', 'date_of_joining']  # Fields to display in the inline

# Inline class to display Statistics instances in the Player admin
class StatisticsInline(admin.StackedInline):  # Using StackedInline for a different layout
    model = Statistics
    can_delete = False  # Disable deleting statistics directly from the player view

# ClubAdmin to manage Club and its related Players
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')  # Display these fields in the club list view
    inlines = [PlayerInline]  # Use the PlayerInline to display players in the Club admin

# PlayerAdmin to manage Player and its related Statistics
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'club', 'national_team', 'position', 'date_of_joining')
    list_filter = ('club', 'position', 'national_team')  # Add filters for club, position, and national_team
    search_fields = ('name', 'club__name', 'national_team__name')  # Enable searching by player's name, club's name, and national team's name
    inlines = [StatisticsInline]  # Use the StatisticsInline to display statistics in the Player admin

# NationalTeamAdmin to manage NationalTeams and Players
class NationalTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'continent')

# FantasyTeamAdmin to manage FantasyTeams and Players
class FantasyTeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('players',)  # Use a horizontal filter for many-to-many relationships with players

# Register the models with their ModelAdmin classes
admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Statistics)
admin.site.register(NationalTeam, NationalTeamAdmin)
admin.site.register(FantasyTeam, FantasyTeamAdmin)
admin.site.register(userModel)


# sarthak : 175sart175