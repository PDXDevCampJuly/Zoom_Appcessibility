from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login_zoom_user, name='log_in'),
    url(r'^property/(?P<property_id>[0-9]+)/$', views.property_description, name='property_description'),
    url(r'^property/(?P<property_id>[0-9]+)/gallery/$', views.property_gallery_page, name='property_gallery'),
    url(r'^property/(?P<property_id>[0-9]+)/gallery/property_gallery', views.property_gallery_page, name='property_gallery'),

    url(r'^new_user', views.new_user, name='new_user'),
    url(r'^homepage_properties', views.properties_listing, name='properties_listing'),
    url(r'^log_out', views.logout, name='log_out'),
    url(r'^about_us', views.about_us, name='about_us'),
    url(r'^contact_us', views.contact_us, name='contact_us'),
    url(r'^privacy_policy', views.privacy_policy, name='privacy_policy'),
    url(r'^terms_of_use', views.terms_of_use, name='terms_of_use'),
    url(r'^new_listing', views.new_listing, name='new_listing'),

]