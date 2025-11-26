from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import TokenError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import (
    Dining, DiningBooking, User, Post, Listing, Donation, Order, OrderItem, Partner, Document
)
from .serializers import (
    DiningBookingSerializer,
    DiningSerializer,
    UserSerializer, 
    BlogPostSerializer, 
    ItemSerializer, 
    DonationSerializer, 
    OrderSerializer, 
    OrderItemSerializer,
    PartnerSerializer,
    DocumentSerializer,
)
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all().order_by('-uploaded_at')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['document_type', 'visibility']
    search_fields = ['file_name', 'description']
    ordering_fields = ['uploaded_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Document.objects.all().order_by('-uploaded_at')
        return Document.objects.filter(visibility='public').order_by('-uploaded_at')

    def get_serializer_class(self):
        user = self.request.user
        if user.is_authenticated:
            from .serializers import DocumentFullSerializer
            return DocumentFullSerializer
        return DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

# User Registration View
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number': user.phone_number,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login View
class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        # Input validation
        email = request.data.get('email', '').strip().lower()
        password = request.data.get('password', '').strip()

        if not email or not password:
            return Response(
                {'error': 'Both email and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Validate email format
            validate_email(email)
        except ValidationError:
            return Response(
                {'error': 'Invalid email format'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Authentication
        try:
            user = authenticate(request=request, email=email, password=password)
            
            if not user:
                return Response(
                    {'error': 'Invalid credentials'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            if not user.is_active:
                return Response(
                    {'error': 'Account is not active'},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Token generation
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number': user.phone_number,
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # Log the error here (e.g., using logging module)
            return Response(
                {'error': 'Authentication failed'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
# User Logout View
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            
            if not refresh_token:
                return Response(
                    {'error': 'Refresh token is required'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            response = Response(
                {'status': 'success', 'message': 'Successfully logged out'},
                status=status.HTTP_200_OK
            )
            
            # Add security headers
            response.delete_cookie('access_token')
            response.delete_cookie('refresh_token')
            return response

        except TokenError as e:
            return Response(
                {'error': 'Invalid refresh token'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        except Exception as e:
            return Response(
                {'error': 'Internal server error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['role', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    ordering_fields = ['date_joined']

# BlogPost ViewSet
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['type', 'slug', 'status', 'published_by']
    search_fields = ['title', 'slug', 'description']
    ordering_fields = ['created_at', 'updated_at']
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(published_by=self.request.user)

# Item ViewSet
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by('created_at')
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['type', 'slug', 'available']
    search_fields = ['title', 'slug', 'description']
    ordering_fields = ['price', 'created_at']
    pagination_class = PageNumberPagination
    lookup_field = 'slug'

class DiningViewSet(viewsets.ModelViewSet):
    queryset = Dining.objects.all().order_by('created_at')
    serializer_class = DiningSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'slug',]
    search_fields = ['title', 'slug', 'location']
    ordering_fields = ['id']
    lookup_field = 'slug'

# Donation ViewSet
class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all().order_by('donated_at')
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['amount', 'email']
    search_fields = ['names', 'email']
    ordering_fields = ['donated_at']

# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'user']
    search_fields = ['user__email']
    ordering_fields = ['created_at', 'total_price']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('id')
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['order', 'item']
    search_fields = ['item__name']
    ordering_fields = ['quantity', 'price']

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all().order_by('id')
    serializer_class = PartnerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id']


class DiningBookingViewSet(viewsets.ModelViewSet):
    queryset = DiningBooking.objects.all().order_by('booking_time')
    serializer_class = DiningBookingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['dining', 'user']
    search_fields = ['dining__name', 'user__email']
    ordering_fields = ['date', 'booking_time']
