from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('now_time/',current_datetime),
    path('greeting/<str:name>/',greeting),
    path('class_view/', Example.as_view()),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', year_archive),
]