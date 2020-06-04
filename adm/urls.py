from django.urls import path
from .views import set_params,checkinfo,setdefault,adm,openclose
urlpatterns = [
    path('set_params', set_params),
    path('index',adm),
    path('checkInfo',checkinfo),
    path('setdefault',setdefault),
    path('openclose',openclose)
]