from django.urls import path
from .views import *

urlpatterns = [
    path('main/',main_page,name='main'),
    path('friends/', all_friends, name='friends'),
    path('establishments/', all_establishment, name='establishments'),

]