from rest_framework import serializers
from .models import userLoanData
from .models import Account

class userLoanDataSerializers(serializers.ModelSerializer):
    class Meta: 
        model = userLoanData
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = '__all__'
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
        
    def save(self):
        account = Account(
            email=self.validated_data['email']
        )
        account.save()
        return account