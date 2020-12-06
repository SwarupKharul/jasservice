from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'customer'

urlpatterns = [
    path('', views.portal, name='customerportal'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

