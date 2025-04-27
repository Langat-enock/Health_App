"""
URL configuration for health_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin      #  should import admin from django
from django.urls import path, include

from main_app import views, api_views
#  from rest_framework.decorators import api_view

urlpatterns = [
    path('register/', views.register_client, name='register_client'),
    path('enroll/<int:program_id>/', views.enroll_in_program, name='enroll_in_program'),
    path('search/', views.ClientSearchView.as_view(), name='client_search'),
    path('profile/', views.client_profile, name='client_profile'),
    path('api/client/<int:pk>/', api_views.ClientProfileAPI.as_view(), name='client_profile_api'),

    path('admin/', admin.site.urls),


]



