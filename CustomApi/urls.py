from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('CustomApi', views.UserLoanView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/checkUser/', views.checkUser),
    path('api/login/', views.Login),
    path('api/register/', views.register),
    path('api/getUserData/', views.getUserData),
]
