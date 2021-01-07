from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import userLoanData
from .serializers import userLoanDataSerializers
import pickle
import json
# import numpy as np
# from sklearn import preprocessing
# import pandas as pd
     

class UserLoanView(viewsets.ModelViewSet):
    queryset = userLoanData.objects.all()
    serializer_class = userLoanDataSerializers

@api_view(["GET"])
def login(request):
    return JsonResponse('Logged In', safe=False)

@api_view(["POST"])
def register(request):
    return

@api_view(["POST"])
def checkUser(request):
    return
	# try:
	# 	mdl=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/loan_model.pkl")
	# 	#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
	# 	mydata=request.data
	# 	unit=np.array(list(mydata.values()))
	# 	unit=unit.reshape(1,-1)
	# 	scalers=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/scalers.pkl")
	# 	X=scalers.transform(unit)
	# 	y_pred=mdl .predict(X)
	# 	y_pred=(y_pred>0.58)
	# 	newdf=pd.DataFrame(y_pred, columns=['Status'])
	# 	newdf=newdf.replace({True:'Approved', False:'Rejected'})
	# 	return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	# except ValueError as e:
	# 	return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

