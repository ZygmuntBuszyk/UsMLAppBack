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
from django.http import HttpResponseBadRequest, HttpResponseForbidden
import numpy as np
import pandas as pd
# from sklearn.externals import joblib
from sklearn import preprocessing
import joblib as jLib


class UserLoanView(viewsets.ModelViewSet):
    queryset = userLoanData.objects.all()
    serializer_class = userLoanDataSerializers


@api_view(["POST"])
def Login(request):
    user_email = request.data['email']
    user_password = request.data['password']
    userTest = authenticate(
        email=request.data['email'], password=request.data['password'])
    try:
        user = Account.objects.get(email=user_email)
        if user_password == user.password:
            return Response(user.email)
        else:
            return HttpResponseForbidden('Wrong password')
    except (Account.DoesNotExist):
        return Response('User does not exist', status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def register(request):
    serializer = AccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'User registered successfully'
    else:
        data = serializer.errors
        return Response(data, status=status.HTTP_400_CONFLICT)
    return Response(data)


@api_view(["POST"])
def getUserData(request):
    user_email = request.data['User']
    try:
        user = Account.objects.get(email=user_email)
        return Response(user.approved)
    except (Account.DoesNotExist):
        return Response('User does not exist', status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def checkUser(request):
    # try:
    userData = request.data
    test = pd.read_pickle(
        "D:/Projects/UsDjangoMlApp/back/RestApi/CustomApi/loan_model.pkl")
    print(userData)
    # mdl = jLib.load(
    #     "C:/Users/stozz/OneDrive/Pulpit/USIproject/backend/UsMLAppBack/CustomApi/loan_model.pkl")

    # mydata = pd.read_excel(
    #     '/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')

    # unit = np.array(list(mydata.values()))
    # unit = unit.reshape(1, -1)
    # scalers = jLib.load(
    #     "C:/Users/stozz/OneDrive/Pulpit/USIproject/backend/UsMLAppBack/CustomApi/scalers.pkl")
    # X = scalers.transform(unit)
    # y_pred = mdl .predict(X)
    # y_pred = (y_pred > 0.58)
    # newdf = pd.DataFrame(y_pred, columns=['Status'])
    # newdf = newdf.replace({True: 'Approved', False: 'Rejected'})
    # return JsonResponse('Your Status is {}'.format(newdf), safe=False)
    return JsonResponse('Your Loan Status is {}'.format(True), safe=False)
    # except ValueError as e:
    #     return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
