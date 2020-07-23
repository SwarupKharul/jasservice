from . import views
from django.urls import path

app_name = 'customer'

urlpatterns = [
    path('', views.portal, name='customerportal'),
    path('info/', views.info, name='info'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
]

