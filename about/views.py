from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import (
    About, Contact, SocialMedia, Team, TeamSocialMedia,
    Slider, Gallery, Video, Testimonial
)
from .serializers import (
    AboutSerializer, ContactSerializer, SocialMediaSerializer,
    TeamSerializer, TeamSocialMediaSerializer, SliderSerializer,
    GallerySerializer, VideoSerializer, TestimonialSerializer
)

class AboutViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for About section"""
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContactViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for Contact section"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TeamViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for Team members"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SocialMediaViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for general Social Media links"""
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TeamSocialMediaViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for Team members' Social Media links"""
    queryset = TeamSocialMedia.objects.all()
    serializer_class = TeamSocialMediaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(active=True)
    serializer_class = SliderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
