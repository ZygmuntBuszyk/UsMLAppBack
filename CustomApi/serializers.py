from rest_framework import serializers
from .models import userLoanData

class userLoanDataSerializers(serializers.ModelSerializer):
    class Meta: 
        model = userLoanData
        fields = '__all__'