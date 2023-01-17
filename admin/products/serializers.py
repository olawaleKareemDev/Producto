from rest_framework import serializers
from .models import Product, User



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



