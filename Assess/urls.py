# urls for Assess app, to deal with evaluation
from django.urls import path
from . import views

urlpatterns = [
    path('evaluation/<nom>/<matr>/', views.show, name="assess"),
    path('classement/<promo>/', views.ranking, name="rank"),
]
