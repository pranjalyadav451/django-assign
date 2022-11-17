from rest_framework import serializers
from .models import Bitcoin, CustomUser


class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = ('coin_name', 'current_price', 'created_at', 'created_by')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'id']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
