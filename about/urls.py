from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutViewSet, ContactViewSet, SocialMediaViewSet,
    TeamViewSet, TeamSocialMediaViewSet, SliderViewSet,
    GalleryViewSet, VideoViewSet, TestimonialViewSet
)

# Create router instance
router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'social-media', SocialMediaViewSet)
router.register(r'team', TeamViewSet)
router.register(r'team-social-media', TeamSocialMediaViewSet)
router.register(r'sliders', SliderViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
