from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Dining, DiningBooking, User as UserModel, Post, Listing, Donation, Order, OrderItem, Partner

User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Use create_user to properly hash the password
        return User.objects.create_user(**validated_data)
    
# BlogPost Serializer
class BlogPostSerializer(serializers.ModelSerializer):
    published_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'short_desc', 'description', 'poster', 'image', 'type', 'published', 'published_by', 'created_at', 'updated_at', 'status']

# Item Serializer
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'slug', 'short_desc', 'description', 'poster', 'image', 'type', 'category', 'price', 'time_frame', 'available', 'created_at']

class DiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dining
        fields = ['id', 'title', 'slug', 'short_desc', 'description', 'poster', 'image', 'location', 'created_at', 'in_use', 'category']

class DiningBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningBooking
        fields = ['id', 'dining', 'user', 'booking_time', 'guests', 'created_at']

# Donation Serializer
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'names', 'email', 'phone_number', 'amount', 'donated_at']

# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'quantity', 'price']

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'items', 'created_at', 'updated_at']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'logo', 'url']