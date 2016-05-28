from django.conf.urls import url

from weddingapp.views import faq_index, faq_practical, faq_cultural

app_name = 'faq'

urlpatterns = [
    url(r'^$', faq_index),
    url(r'^practical/$', faq_practical, name='faq_practical'),
    url(r'^cultural/$', faq_cultural, name='faq_cultural'),
]
