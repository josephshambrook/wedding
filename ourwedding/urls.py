from django.conf.urls import include, url
from django.contrib import admin

from weddingapp.views import home_view

urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^rsvp/', include('weddingapp.rsvp_urls')),
    url(r'^faq/', include('weddingapp.faq_urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]