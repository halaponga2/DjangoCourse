from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ShopSerializer, GoodsSerializer
from .models import Shop, Goods
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class GoodsViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type']
    search_fields = ['type','name']


    @action(methods=['GET'], detail=False)
    def drinks(self,request):
        drinks = Goods.objects.filter(Q(type="Газировка") | Q(type="Молочка"))
        data = GoodsSerializer(drinks, many=True).data
        return Response(data)

    @action(methods=['POST'], detail=True)
    def addshop(self,request, pk=None):
        if 'shop_id' not in request.data:
            raise ValidationError ({'shop_id': 'Необходим id магазина'})
        
        shop_id = request.data['shop_id']
        if Goods.objects.filter(shops= shop_id, pk=pk).exists():
            raise ValidationError ({'shop_id': 'Магазин уже привязан'})


        try:
            shop = Shop.objects.get(id = shop_id)
        except Shop.DoesNotExist:
            raise ValidationError ({'shop_id': 'Указанного магазина не существует'})
        goods = Goods.objects.get(pk=pk)
        goods.shops.add(shop)
        data = GoodsSerializer(goods).data
        return Response (data)

    

