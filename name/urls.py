from django.conf.urls import url
from name.views import BaseIndexView


urlpatterns = [
    url(r'^$', BaseIndexView.as_view(), name='index'),
]
