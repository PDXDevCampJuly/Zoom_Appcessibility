from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.login_zoom_user, name='log_in'),
    url(r'^homepage_properties', views.properties_listing, name='properties_listing'),
    url(r'^big_description', views.big_description_page, name='big_description'),
    url(r'^property_gallery', views.property_gallery_page, name='property_gallery'),
    url(r'^about_us', views.about_us, name='about_us'),
    url(r'^contact_us', views.contact_us, name='contact_us'),
    url(r'^privacy_policy', views.privacy_policy, name='privacy_policy'),
    url(r'^terms_of_use', views.terms_of_use, name='terms_of_use'),
    url(r'^new_listing', views.new_listing, name='new_listing'),

]