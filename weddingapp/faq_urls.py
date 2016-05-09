from django.conf.urls import url

from weddingapp.views import faq_index, faq_practical, faq_cultural

app_name = 'weddingapp'

urlpatterns = [
    url(r'^$', faq_index),
    url(r'^practical', faq_practical),
    url(r'^cultural', faq_cultural)
]
