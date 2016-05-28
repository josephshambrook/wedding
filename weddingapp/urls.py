from django.conf.urls import url, include

from weddingapp.views import home_view

app_name = 'weddingapp'

urlpatterns = [
    # url(r'^$', home_view, name='home'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
]