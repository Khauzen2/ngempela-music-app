from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ngempela/', views.ngempela, name='ngempela'), # music page
    path('about/', views.about, name='about'), # about page
    path('contact/', views.contact, name='contact'),  # Contact page
]