from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', include('weddingapp.urls')),
    url(r'^rsvp/', include('weddingapp.rsvp_urls')),
    url(r'^faq/', include('weddingapp.faq_urls')),
    url(r'^admin/', admin.site.urls),
]