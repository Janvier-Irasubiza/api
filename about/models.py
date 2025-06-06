from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

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

class Slider(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='sliders/',
        help_text='Upload slider image',
        null=True,
        blank=True
    )
    action = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        choices=[
            ('join', 'Join'),
            ('donate', 'Donate'),
            ('none', 'None'),
        ],
        default='none'
    )
    action_text = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text='This is the text that will be displayed on the button [Make Impact, Join Us, Donate, etc.]. but make it short and concise'
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.image:
            raise ValidationError({'image': 'Image is required for Slider'})
        if self.action != 'none' and not self.action_text:
            raise ValidationError({'action_text': 'Action text is required when an action is selected'})

    def save(self, *args, **kwargs):
        self.clean()
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            print(f"Error saving Slider: {str(e)}")
            raise

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sliders'
        verbose_name = 'Slider'
        ordering = ['-created_at']

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Gallery'
        verbose_name = 'Gallery'

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(help_text='This is the description of the video. make it short and concise')
    url = models.URLField(help_text='This is the url of the video. if it is youtube, make sure to use the embed url')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name