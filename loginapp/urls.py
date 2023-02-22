from django.urls import path

from .views import Loginviewset,LoginView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('loginapi',Loginviewset,basename='Userprofile')
urlpatterns = [
   # path('api/login/', LoginView.as_view()),
    path('api/loginapi/',Loginviewset)
]+router.urls