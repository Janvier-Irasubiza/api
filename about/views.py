from rest_framework import viewsets
from .models import About, Team, SocialMedia, TeamSocialMedia, Contact
from .serializers import AboutSerializer, TeamSerializer, SocialMediaSerializer, TeamSocialMediaSerializer, ContactSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

class AboutViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for About section"""
    queryset = About.objects.all().order_by('-created_at')
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContactViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for Contact section"""
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TeamViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for Team members"""
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SocialMediaViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for general Social Media links"""
    queryset = SocialMedia.objects.all().order_by('name')
    serializer_class = SocialMediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TeamSocialMediaViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for Team members' Social Media links"""
    queryset = TeamSocialMedia.objects.all().order_by('name')
    serializer_class = TeamSocialMediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
