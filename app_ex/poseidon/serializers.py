from rest_framework import serializers
from app_ex.poseidon.models import Commodity, CommodityCategory


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'
