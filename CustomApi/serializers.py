from rest_framework import serializers
from .models import userLoanData
from .models import Account
from django.contrib.auth import authenticate

class userLoanDataSerializers(serializers.ModelSerializer):
    class Meta: 
        model = userLoanData
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        account = Account(
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
        account.save()
        return account

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'password']