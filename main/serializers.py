from rest_framework import serializers
from .models import Shop, Goods

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

    

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"

    def validate_price(self, value):
        if value>10000:
            raise serializers.ValidationError("Цена не может быть настолько большой")
        return value