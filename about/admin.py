from django.contrib import admin
from .models import About, Team, SocialMedia, TeamSocialMedia, Contact

admin.site.register([About, Team, SocialMedia, TeamSocialMedia, Contact])