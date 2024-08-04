from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        # field=['id','name','description','price','stock','created_at','updated_at']    
        fields = '__all__'
