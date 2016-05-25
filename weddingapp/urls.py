from django.conf.urls import url, include

from weddingapp.views import index_view, welcome_view, attend_view, extra_view, confirm_view, finish_view

app_name = 'weddingapp'

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^(?P<code>[0-9]+)/$', welcome_view, name='welcome'),
    url(r'^(?P<code>[0-9]+)/attend$', attend_view, name='attend'),
    url(r'^(?P<code>[0-9]+)/extra$', extra_view, name='extra'),
    url(r'^(?P<code>[0-9]+)/confirm$', confirm_view, name='confirm'),
    url(r'^(?P<code>[0-9]+)/finish$', finish_view, name='finish'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
]