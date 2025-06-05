from rest_framework import serializers
from .models import (
    About, Contact, SocialMedia, Team, TeamSocialMedia,
    Slider, Gallery, Video, Testimonial
)

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TeamSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSocialMedia
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    social_links = TeamSocialMediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Team
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    name_display = serializers.CharField(source='get_name_display', read_only=True)

    class Meta:
        model = SocialMedia
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'