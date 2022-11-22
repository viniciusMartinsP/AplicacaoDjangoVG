from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

app_name='exemplo'

urlpatterns = [
    path('exemplo', views.get_boostrap, name='get_boostrap'),
    path('exemplo/collapse', views.collapse, name='collapse'),
    path('exemplo/flexbox', views.flexbox, name='flexbox'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

