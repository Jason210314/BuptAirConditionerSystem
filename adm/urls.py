from django.urls import path
from django.conf.urls import url
from .views import set_params,checkinfo,setdefault,adm,openclose
urlpatterns = [
    path('settemp', set_params),
    path('index',adm),
    path('checkInfo',checkinfo),
    path('setdefault',setdefault),
    path('openclose',openclose),
]