from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^homepage_properties', views.properties_listing, name='properties_listing'),
]