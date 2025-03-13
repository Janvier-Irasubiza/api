from django.db import models
from django.utils.translation import gettext_lazy as _

# Enum for social media choices
class SocialChoices(models.TextChoices):
    FACEBOOK = 'Facebook', _('Facebook')
    TWITTER = 'Twitter', _('Twitter')
    INSTAGRAM = 'Instagram', _('Instagram')
    LINKEDIN = 'LinkedIn', _('LinkedIn')
    YOUTUBE = 'YouTube', _('YouTube')
    WHATSAPP = 'WhatsApp', _('WhatsApp')
    TELEGRAM = 'Telegram', _('Telegram')

# About model
class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else "About Section"

    class Meta:
        verbose_name_plural = 'About'

# Contact model
class Contact(models.Model):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Contact'

# Social Media model (General)
class SocialMedia(models.Model):
    name = models.CharField(
        max_length=100, 
        choices=SocialChoices.choices, 
        default=SocialChoices.FACEBOOK
    )
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_name_display()} - {self.link}"

    class Meta:
        verbose_name_plural = 'UrugoWoc Social Media'
        verbose_name = 'UrugoWoc Social Media'

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Team'

# Social Media linked to Team Members
class TeamSocialMedia(models.Model):
    name = models.CharField(
        max_length=100, 
        choices=SocialChoices.choices, 
        default=SocialChoices.FACEBOOK
    )
    link = models.URLField()
    team_member = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='social_links')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team_member.name} - {self.get_name_display()}"

    class Meta:
        verbose_name_plural = 'Team Social Media'
