# from django.urls import path

# from .views import Loginviewset,LoginView
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('loginapi',Loginviewset,basename='Userprofile')
# urlpatterns = [
#     path('login/', LoginView.as_view()),

# ]
from django.urls import path
from .views import RegistrationAPIView

urlpatterns = [
    path('LoginApi/', RegistrationAPIView.as_view()),
]
