"""jasservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from home import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),
    path('insurance/', views.insurance, name='insurance'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('career/', views.career, name='career'),
    path('loan/', views.loan, name='loan'),
    path('property/', views.property, name='property'),
    path('suggestion/', views.suggestion, name='suggestion'),
    path('sendemail/', views.sendemail, name='sendemail'),
    # User
    #path('customer/', include('customer.urls', namespace="customer")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

