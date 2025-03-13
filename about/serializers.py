from rest_framework import serializers
from .models import About, Team, SocialMedia, TeamSocialMedia, Contact

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TeamSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSocialMedia
        fields = ['id', 'name', 'link', 'created_at', 'updated_at']

class TeamSerializer(serializers.ModelSerializer):
    social_links = TeamSocialMediaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'role', 'image', 'social_links', 'created_at', 'updated_at']


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