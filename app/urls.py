from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    DiningBookingViewSet,
    UserViewSet,
    BlogPostViewSet,
    ItemViewSet,
    DonationViewSet,
    OrderViewSet,
    OrderItemViewSet,
    RegisterView,
    LoginView,
    PartnerViewSet,
    DiningViewSet,
)

# Initialize router
router = DefaultRouter()

# Register viewsets
router.register(r'users', UserViewSet)
router.register(r'blog-posts', BlogPostViewSet)
router.register(r'listings', ItemViewSet)
router.register(r'dining', DiningViewSet)
router.register(r'dining-bookings', DiningBookingViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'partners', PartnerViewSet)

# URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]