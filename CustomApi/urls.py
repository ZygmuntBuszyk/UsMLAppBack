from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('CustomApi', views.UserLoanView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/checkUser/', views.checkUser),
    path('api/login/', views.login),
    path('api/register/', views.register),

]   

# router = routers.DefaultRouter()
# router.register(r'users',views.UserViewSet)                                                                         

# urlpatterns = [ 
#     path('', views.dash, name='dash'),
#     path('api/', include(router.urls)),
#     path('api/instances/', views.InstanceList.as_view(), name="instances"),
# ]