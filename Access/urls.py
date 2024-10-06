# urls for Access app, to deal with identities' validation
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="validate")
]
