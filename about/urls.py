from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, TeamViewSet, SocialMediaViewSet, ContactViewSet

# Create router instance
router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'team', TeamViewSet)
router.register(r'social-media', SocialMediaViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
