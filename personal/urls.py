from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home_screen_view, name='personal')

]
