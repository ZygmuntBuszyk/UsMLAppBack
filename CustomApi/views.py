from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import userLoanData, Account
from .serializers import userLoanDataSerializers
import pickle
import json
from .serializers import AccountSerializer, LoginSerializer
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.core import serializers
# import numpy as np
# from sklearn import preprocessing
# import pandas as pd
     

class UserLoanView(viewsets.ModelViewSet):
    queryset = userLoanData.objects.all()
    serializer_class = userLoanDataSerializers

@api_view(["POST"])
def Login(request):
	user_email = request.data['email']
	user_password = request.data['password']
	userTest = authenticate(email=request.data['email'], password=request.data['password'])
	try:
		user = Account.objects.get(email=user_email)
		if user_password == user.password:
			return Response(user.email)
		else:
			return Response('Wrong password')
	except (Account.DoesNotExist):
		return Response('User does not exist')

@api_view(["POST"])
def register(request):	
	serializer =  AccountSerializer(data=request.data)
	data = {}
	if serializer.is_valid():
		account = serializer.save()
		data['response'] = 'User registered successfully'
	else:
		data = serializer.errors
	return Response(data)

@api_view(["POST"])
def checkUser(request):
    return