from django.urls import path
from about.views import about,faq
urlpatterns = [
    path('',about,name='about'),
    path('faq/',faq,name='faq')
]
