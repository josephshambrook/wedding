from django.conf.urls import url

from weddingapp.views import index_view, attend_view, extra_view, confirm_view, finish_view

app_name = 'weddingapp'

urlpatterns = [
    # url(r'^(?P<code>[0-9]+)/$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # url(r'^rsvp/$', views.RsvpHome.as_view(), name='rsvp'),

    # url(r'^(?P<code>[0-9]+)/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<code>[0-9]+)/$', index_view, name='index'),
    url(r'^(?P<code>[0-9]+)/attend$', attend_view, name='attend'),
    url(r'^(?P<code>[0-9]+)/extra$', extra_view, name='extra'),
    url(r'^(?P<code>[0-9]+)/confirm$', confirm_view, name='confirm'),
    url(r'^(?P<code>[0-9]+)/finish', finish_view, name='finish'),


]
