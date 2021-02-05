from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    #모델 연결
    class Meta:
        model = Product
        fields = '__all__' # 자동으로 모델 안에 있는 모든 필드들을 가지고 옴
        