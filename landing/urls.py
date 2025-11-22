from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('contato/', views.contato_submit, name='contato_submit'),
    path('contato/sucesso/', views.contato_success, name='contato_success'),
    path('contato/form/', views.contato_form_view, name='contato_form'),
]