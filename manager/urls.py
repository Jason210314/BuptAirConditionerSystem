'''
@Author: your name
@Date: 2020-06-01 16:17:42
@LastEditTime: 2020-06-01 17:44:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /django-air/manager/urls.py
'''
from django.urls import path, include
from .views import index

urlpatterns = [
    path('index', index)
]